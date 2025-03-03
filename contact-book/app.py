#type: ignore
import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import re
import uuid


CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def is_valid_phone(phone):
    return phone.replace(' ', '').replace('-', '').replace('+', '').replace('(', '').replace(')', '').isdigit()

def is_valid_email(email):
    if not email:
        return True
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def format_phone(phone):
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone

def main():
    
    st.set_page_config(page_title="Professional Contact Manager", page_icon="📇", layout="wide")

    if 'contacts' not in st.session_state:
        st.session_state.contacts = load_contacts()

  
    if 'phone_numbers' not in st.session_state:
        st.session_state.phone_numbers = [""]
    
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ""
        
    if 'show_form_feedback' not in st.session_state:
        st.session_state.show_form_feedback = False
    
    if 'form_success' not in st.session_state:
        st.session_state.form_success = False
    
    if 'form_message' not in st.session_state:
        st.session_state.form_message = ""

    
    st.title("📇 Professional Contact Manager")
    st.markdown("Manage your contacts efficiently with this enhanced application")

    st.markdown("""
    <style>
    .contact-card {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        border: 1px solid #ddd;
    }
    .stButton button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        
        menu = ["Add Contact", "View Contacts", "Update Contact", "Delete Contact", "Search Contacts", "Export/Import", "Clear All"]
        choice = st.selectbox("Menu", menu)
        
       
        st.subheader("Contact Statistics")
        st.metric("Total Contacts", len(st.session_state.contacts))
        

        if st.session_state.contacts:
            unique_emails = len([c for c in st.session_state.contacts.values() if c.get('email')])
            st.metric("Contacts with Email", unique_emails)

    if st.session_state.show_form_feedback:
        if st.session_state.form_success:
            st.success(st.session_state.form_message)
        else:
            st.error(st.session_state.form_message)
        st.session_state.show_form_feedback = False

    if choice == "Add Contact":
        st.subheader("Add New Contact")
        
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name")
        
        with col2:
            email = st.text_input("Email (optional)")
        
        st.subheader("Phone Numbers")
        
        phone_numbers = st.session_state.phone_numbers.copy()
        

        for i in range(len(phone_numbers)):
            col1, col2 = st.columns([4, 1])
            with col1:
                phone_numbers[i] = st.text_input(
                    f"Phone Number {i+1}", 
                    value=phone_numbers[i], 
                    key=f"phone_{i}",
                    placeholder="(123) 456-7890"
                ).strip()
            with col2:
                if len(phone_numbers) > 1 and st.button("🗑️", key=f"remove_{i}", help="Remove this number"):
                    phone_numbers.pop(i)
                    st.session_state.phone_numbers = phone_numbers
                    st.rerun()

        if st.button("➕ Add Another Number", key="add_number"):
            phone_numbers.append("")
            st.session_state.phone_numbers = phone_numbers
            st.rerun()
            
        notes = st.text_area("Notes (optional)", placeholder="Add any additional information about this contact")
            
        tags = st.text_input("Tags (comma separated)", placeholder="work, family, important")
       
        if st.button("Add Contact", type="primary"):
            st.session_state.phone_numbers = phone_numbers 
            
          
            if not name:
                st.session_state.show_form_feedback = True
                st.session_state.form_success = False
                st.session_state.form_message = "Name is required!"
                st.rerun()
                
            elif not is_valid_email(email):
                st.session_state.show_form_feedback = True
                st.session_state.form_success = False
                st.session_state.form_message = "Invalid email format!"
                st.rerun()
                
            else:
                phones = [p.strip() for p in phone_numbers if p.strip()]
                valid_phones = all(is_valid_phone(p) for p in phones)
                
                if not phones:
                    st.session_state.show_form_feedback = True
                    st.session_state.form_success = False
                    st.session_state.form_message = "At least one phone number is required!"
                    st.rerun()
                    
                elif not valid_phones:
                    st.session_state.show_form_feedback = True
                    st.session_state.form_success = False
                    st.session_state.form_message = "Invalid phone number format!"
                    st.rerun()
                    
                else:
                    
                    tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()] if tags else []
                    
                    
                    contact_id = str(uuid.uuid4())
                    
                    
                    if name in st.session_state.contacts:
                        
                        contact_id = st.session_state.contacts[name].get('id', contact_id)
                        existing_phones = st.session_state.contacts[name]['phones']
                        existing_phones.extend(phones)
                        unique_phones = list(set(existing_phones))
                        
                        
                        existing_tags = st.session_state.contacts[name].get('tags', [])
                        merged_tags = list(set(existing_tags + tag_list))
                        
                        st.session_state.contacts[name] = {
                            'id': contact_id,
                            'email': email,
                            'phones': unique_phones,
                            'notes': notes,
                            'tags': merged_tags,
                            'created_at': st.session_state.contacts[name]['created_at'],
                            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        st.session_state.show_form_feedback = True
                        st.session_state.form_success = True
                        st.session_state.form_message = f"Contact {name} updated successfully!"
                        
                    else:
                        st.session_state.contacts[name] = {
                            'id': contact_id,
                            'email': email,
                            'phones': phones,
                            'notes': notes,
                            'tags': tag_list,
                            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        st.session_state.show_form_feedback = True
                        st.session_state.form_success = True
                        st.session_state.form_message = f"Contact {name} added successfully!"
                    
                    
                    save_contacts(st.session_state.contacts)
                    
                   
                    st.session_state.phone_numbers = [""]
                    st.rerun()

    elif choice == "View Contacts":
        st.subheader("All Contacts")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            view_type = st.radio("View as", ["Table", "Cards"])
        
        if st.session_state.contacts:
           
            filtered_contacts = {}
           
            filtered_contacts = st.session_state.contacts
                
            if view_type == "Table":
                data = []
                for name, info in filtered_contacts.items():
                    data.append({
                        "Name": name,
                        "Email": info.get('email', ''),
                        "Phone Numbers": ", ".join([format_phone(p) for p in info.get('phones', [])]),
                        "Tags": ", ".join(info.get('tags', [])),
                        "Created": info.get('created_at', '')
                    })
                    
                if data:
                    df = pd.DataFrame(data)
                    st.dataframe(df, use_container_width=True, height=400)
                else:
                    st.info("No contacts match your filter criteria!")
            
            else:
                if filtered_contacts:
                    rows = [list(filtered_contacts.items())[i:i+3] for i in range(0, len(filtered_contacts), 3)]
                    
                    for row in rows:
                        cols = st.columns(3)
                        for i, (name, info) in enumerate(row):
                            with cols[i]:
                                st.markdown(f"""
                                <div class="contact-card">
                                    <h3>{name}</h3>
                                    <p>Email: {info.get('email', 'N/A')}</p>
                                    <p>Phone: {format_phone(info.get('phones', [''])[0]) if info.get('phones') else 'N/A'}</p>
                                    <p>Tags: {', '.join(info.get('tags', ['None']))}</p>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                if st.button("View Details", key=f"view_{info.get('id', name)}"):
                                    st.session_state.selected_contact = name
                                    st.rerun()
                                    
                    
                    if 'selected_contact' in st.session_state and st.session_state.selected_contact:
                        selected = st.session_state.selected_contact
                        if selected in st.session_state.contacts:
                            info = st.session_state.contacts[selected]
                            
                            st.markdown("---")
                            st.subheader(f"Contact Details: {selected}")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.write("**Email:**", info.get('email', 'N/A'))
                                st.write("**Created:**", info.get('created_at', 'N/A'))
                                st.write("**Updated:**", info.get('updated_at', 'N/A'))
                                st.write("**Tags:**", ", ".join(info.get('tags', ['None'])))
                                
                            with col2:
                                st.write("**Phone Numbers:**")
                                for phone in info.get('phones', []):
                                    st.write(f"- {format_phone(phone)}")
                            
                            st.write("**Notes:**")
                            st.write(info.get('notes', 'No notes available'))
                            
                            if st.button("Close Details"):
                                del st.session_state.selected_contact
                                st.rerun()
                else:
                    st.info("No contacts match your filter criteria!")
        else:
            st.info("No contacts found. Add some contacts first!")

    
    elif choice == "Update Contact":
        st.subheader("Update Existing Contact")
        
        if st.session_state.contacts:
            
            contact_to_update = st.selectbox("Select Contact", list(st.session_state.contacts.keys()))
            
            if contact_to_update:
              
                if 'update_phone_numbers' not in st.session_state or st.session_state.get('last_updated_contact') != contact_to_update:
                    st.session_state.update_phone_numbers = st.session_state.contacts[contact_to_update].get('phones', []).copy()
                    st.session_state.last_updated_contact = contact_to_update
                
                
                col1, col2 = st.columns(2)
                
                with col1:
                    new_name = st.text_input("Name", value=contact_to_update)
                
                with col2:
                    new_email = st.text_input("Email", value=st.session_state.contacts[contact_to_update].get('email', ''))
                
                st.subheader("Phone Numbers")
                
                update_phone_numbers = st.session_state.update_phone_numbers.copy()
                if not update_phone_numbers:
                    update_phone_numbers = [""]
                
                for i in range(len(update_phone_numbers)):
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        update_phone_numbers[i] = st.text_input(
                            f"Phone Number {i+1}",
                            value=update_phone_numbers[i],
                            key=f"update_phone_{i}",
                            placeholder="(123) 456-7890"
                        ).strip()
                    with col2:
                        if len(update_phone_numbers) > 1 and st.button("🗑️", key=f"update_remove_{i}", help="Remove this number"):
                            update_phone_numbers.pop(i)
                            st.session_state.update_phone_numbers = update_phone_numbers
                            st.rerun()
                
                if st.button("➕ Add Another Number", key="update_add_number"):
                    update_phone_numbers.append("")
                    st.session_state.update_phone_numbers = update_phone_numbers
                    st.rerun()
                
                
                current_notes = st.session_state.contacts[contact_to_update].get('notes', '')
                notes = st.text_area("Notes (optional)", value=current_notes)
                
                
                current_tags = ", ".join(st.session_state.contacts[contact_to_update].get('tags', []))
                tags = st.text_input("Tags (comma separated)", value=current_tags)
                
                
                if st.button("Update Contact", type="primary"):
                    st.session_state.update_phone_numbers = update_phone_numbers
                    
                   
                    if not new_name:
                        st.session_state.show_form_feedback = True
                        st.session_state.form_success = False
                        st.session_state.form_message = "Name is required!"
                        st.rerun()
                        
                    elif not is_valid_email(new_email):
                        st.session_state.show_form_feedback = True
                        st.session_state.form_success = False
                        st.session_state.form_message = "Invalid email format!"
                        st.rerun()
                        
                    else:
                        phones = [p.strip() for p in update_phone_numbers if p.strip()]
                        valid_phones = all(is_valid_phone(p) for p in phones)
                        
                        if not phones:
                            st.session_state.show_form_feedback = True
                            st.session_state.form_success = False
                            st.session_state.form_message = "At least one phone number is required!"
                            st.rerun()
                            
                        elif not valid_phones:
                            st.session_state.show_form_feedback = True
                            st.session_state.form_success = False
                            st.session_state.form_message = "Invalid phone number format!"
                            st.rerun()
                            
                        else:
                            
                            tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()] if tags else []
                            
                            
                            contact_id = st.session_state.contacts[contact_to_update].get('id', str(uuid.uuid4()))
                            
                            
                            if new_name != contact_to_update:
                                if new_name in st.session_state.contacts and new_name != contact_to_update:
                                    st.session_state.show_form_feedback = True
                                    st.session_state.form_success = False
                                    st.session_state.form_message = f"Contact with name '{new_name}' already exists!"
                                    st.rerun()
                                else:
                                    del st.session_state.contacts[contact_to_update]
                            
                            
                            st.session_state.contacts[new_name] = {
                                'id': contact_id,
                                'email': new_email,
                                'phones': phones,
                                'notes': notes,
                                'tags': tag_list,
                                'created_at': st.session_state.contacts.get(contact_to_update, {}).get('created_at',
                                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            }
                            
                            
                            save_contacts(st.session_state.contacts)
                            
                            
                            st.session_state.show_form_feedback = True
                            st.session_state.form_success = True
                            st.session_state.form_message = f"Contact updated successfully!"
                            
                           
                            del st.session_state.update_phone_numbers
                            del st.session_state.last_updated_contact
                            st.rerun()
        else:
            st.info("No contacts available to update!")

    
    elif choice == "Delete Contact":
        st.subheader("Delete Contact")
        
        if st.session_state.contacts:
            contact_to_delete = st.selectbox("Select Contact to Delete", list(st.session_state.contacts.keys()))
            
            if contact_to_delete:
               
                contact_info = st.session_state.contacts[contact_to_delete]
                
                st.warning(f"Are you sure you want to delete the contact '{contact_to_delete}'?")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Email:**", contact_info.get('email', 'N/A'))
                with col2:
                    st.write("**Phone:**", ", ".join([format_phone(p) for p in contact_info.get('phones', [])]))
                
                if st.button("🗑️ Delete Contact", key='delete_button', type="primary"):
                    del st.session_state.contacts[contact_to_delete]
                    save_contacts(st.session_state.contacts)
                    
                    st.session_state.show_form_feedback = True
                    st.session_state.form_success = True
                    st.session_state.form_message = f"Contact {contact_to_delete} deleted successfully!"
                    st.rerun()
        else:
            st.info("No contacts available to delete!")

    
    elif choice == "Search Contacts":
        st.subheader("Search Contacts")
        
        search_query = st.text_input("Search by name, email, phone, or tags", value=st.session_state.search_query)
        st.session_state.search_query = search_query
        
        if search_query:
            search_results = {}
            
            for name, info in st.session_state.contacts.items():
            
                if search_query.lower() in name.lower():
                    search_results[name] = info
                    continue
               
                if info.get('email') and search_query.lower() in info.get('email').lower():
                    search_results[name] = info
                    continue
               
                if any(search_query in phone for phone in info.get('phones', [])):
                    search_results[name] = info
                    continue
                    
               
                if any(search_query.lower() in tag.lower() for tag in info.get('tags', [])):
                    search_results[name] = info
                    continue
                    
            
                if info.get('notes') and search_query.lower() in info.get('notes').lower():
                    search_results[name] = info
                    continue
            
            if search_results:
                st.write(f"Found {len(search_results)} matching contacts:")
                
               
                for name, info in search_results.items():
                    with st.expander(f"{name} - {info.get('email', 'No Email')}"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write("**Phone Numbers:**")
                            for phone in info.get('phones', []):
                                st.write(f"- {format_phone(phone)}")
                                
                            st.write("**Tags:**", ", ".join(info.get('tags', ['None'])))
                            
                        with col2:
                            st.write("**Created:**", info.get('created_at', 'N/A'))
                            st.write("**Last Updated:**", info.get('updated_at', 'N/A'))
                            
                        st.write("**Notes:**")
                        st.write(info.get('notes', 'No notes available'))
                        
                        col1, col2 = st.columns(2)
            else:
                st.info(f"No contacts found matching '{search_query}'")
        elif st.session_state.contacts:
            st.write(f"Enter search terms to find contacts.")
        else:
            st.info("No contacts available to search!")

    
    elif choice == "Export/Import":
        st.subheader("Export/Import Contacts")
        
        tab1, tab2 = st.tabs(["Export", "Import"])
        
        with tab1:
            st.write("Export your contacts to different formats")
            
            export_format = st.radio("Select export format", ["JSON", "CSV"])
            
            if st.button("Export Contacts"):
                if not st.session_state.contacts:
                    st.warning("No contacts to export!")
                else:
                    if export_format == "JSON":
                       
                        json_str = json.dumps(st.session_state.contacts, indent=4)
                        st.download_button(
                            label="Download JSON",
                            data=json_str,
                            file_name="contacts_export.json",
                            mime="application/json"
                        )
                    else:
                    
                        data = []
                        for name, info in st.session_state.contacts.items():
                            row = {
                                "Name": name,
                                "Email": info.get('email', ''),
                                "Phone Numbers": ";".join(info.get('phones', [])),
                                "Tags": ";".join(info.get('tags', [])),
                                "Notes": info.get('notes', ''),
                                "Created": info.get('created_at', ''),
                                "Updated": info.get('updated_at', '')
                            }
                            data.append(row)
                            
                        df = pd.DataFrame(data)
                        csv = df.to_csv(index=False)
                        
                        st.download_button(
                            label="Download CSV",
                            data=csv,
                            file_name="contacts_export.csv",
                            mime="text/csv"
                        )
        
        with tab2:
            st.write("Import contacts from a file")
            
            import_file = st.file_uploader("Upload a JSON or CSV file", type=["json", "csv"])
            
            if import_file is not None:
                import_type = import_file.name.split('.')[-1].lower()
                
                if import_type == "json":
                    try:
                        imported_contacts = json.loads(import_file.getvalue().decode())
                        
                        if isinstance(imported_contacts, dict):
                            if st.button("Confirm Import"):
                                
                                for name, info in imported_contacts.items():
                                    if name in st.session_state.contacts:
                                      
                                        combined_phones = list(set(st.session_state.contacts[name].get('phones', []) + info.get('phones', [])))
                                        combined_tags = list(set(st.session_state.contacts[name].get('tags', []) + info.get('tags', [])))
                                        
                                        st.session_state.contacts[name] = {
                                            'id': st.session_state.contacts[name].get('id', str(uuid.uuid4())),
                                            'email': info.get('email', st.session_state.contacts[name].get('email', '')),
                                            'phones': combined_phones,
                                            'notes': info.get('notes', st.session_state.contacts[name].get('notes', '')),
                                            'tags': combined_tags,
                                            'created_at': st.session_state.contacts[name].get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        }
                                    else:
                                        
                                        st.session_state.contacts[name] = {
                                            'id': info.get('id', str(uuid.uuid4())),
                                            'email': info.get('email', ''),
                                            'phones': info.get('phones', []),
                                            'notes': info.get('notes', ''),
                                            'tags': info.get('tags', []),
                                            'created_at': info.get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        }
                                
                                save_contacts(st.session_state.contacts)
                                st.session_state.show_form_feedback = True
                                st.session_state.form_success = True
                                st.session_state.form_message = f"Successfully imported {len(imported_contacts)} contacts!"
                                st.rerun()
                        else:
                            st.error("Invalid JSON format. Expected a dictionary.")
                    except Exception as e:
                        st.error(f"Error parsing JSON file: {str(e)}")
                
                elif import_type == "csv":
                    try:
                        df = pd.read_csv(import_file)
                        
                        if "Name" in df.columns:
                            st.write(f"Found {len(df)} contacts in the CSV file")
                            st.dataframe(df.head())
                            
                            if st.button("Confirm Import"):
                                imported_count = 0
                                
                                for _, row in df.iterrows():
                                    name = row.get("Name")
                                    if not name or pd.isna(name):
                                        continue
                                        
                                 
                                    phone_str = row.get("Phone Numbers", "")
                                    phones = phone_str.split(";") if not pd.isna(phone_str) else []
                                    phones = [p.strip() for p in phones if p.strip()]
                                    
                                  
                                    tag_str = row.get("Tags", "")
                                    tags = tag_str.split(";") if not pd.isna(tag_str) else []
                                    tags = [t.strip() for t in tags if t.strip()]
                                    
                                   
                                    contact_data = {
                                        'id': str(uuid.uuid4()),
                                        'email': str(row.get("Email", "")) if not pd.isna(row.get("Email", "")) else "",
                                        'phones': phones,
                                        'notes': str(row.get("Notes", "")) if not pd.isna(row.get("Notes", "")) else "",
                                        'tags': tags,
                                        'created_at': str(row.get("Created", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) if not pd.isna(row.get("Created", "")) else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    }
                                    
                                    st.session_state.contacts[name] = contact_data
                                    imported_count += 1
                                
                                save_contacts(st.session_state.contacts)
                                st.session_state.show_form_feedback = True
                                st.session_state.form_success = True
                                st.session_state.form_message = f"Successfully imported {imported_count} contacts!"
                                st.rerun()
                        else:
                            st.error("Invalid CSV format. Required column 'Name' not found.")
                    except Exception as e:
                        st.error(f"Error parsing CSV file: {str(e)}")

  
    elif choice == "Clear All":
        st.subheader("Clear All Contacts")
        
        if st.session_state.contacts:
            st.warning("⚠️ This action will permanently delete all your contacts!")
            
            confirm_text = st.text_input("Type 'DELETE ALL CONTACTS' to confirm:")
            
            if confirm_text == "DELETE ALL CONTACTS" and st.button("Permanently Delete All Contacts", type="primary"):
                st.session_state.contacts = {}
                save_contacts(st.session_state.contacts)
           
                if os.path.exists(CONTACTS_FILE):
                    os.remove(CONTACTS_FILE)
                
                st.session_state.show_form_feedback = True
                st.session_state.form_success = True
                st.session_state.form_message = "All contacts cleared successfully!"
                st.rerun()
        else:
            st.info("No contacts to clear!")

    st.markdown("---")
    st.markdown("📇 Professional Contact Manager v2.0 | Created with Streamlit")

if __name__ == '__main__':
    main()