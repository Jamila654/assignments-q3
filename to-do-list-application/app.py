#type:ignore
import streamlit as st
import json
import os
from datetime import datetime

TODO_FILE = "todo_lists.json"

def load_todo_lists():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_todo_lists(todo_lists):
    with open(TODO_FILE, 'w') as f:
        json.dump(todo_lists, f)


def main():
    st.set_page_config("To-Do App", layout="centered")
    st.title("Multi-List To-Do App")

    if 'todo_lists' not in st.session_state:
        st.session_state.todo_lists = load_todo_lists()

    with st.sidebar:
        st.header("List Management")
        
        new_list_name = st.text_input("New List Name")
        if st.button("Add List") and new_list_name:
            if new_list_name not in st.session_state.todo_lists:
                st.session_state.todo_lists[new_list_name] = []
                save_todo_lists(st.session_state.todo_lists)
                st.success(f"List '{new_list_name}' created!")
            else:
                st.error("List name already exists!")

        selected_list = st.selectbox(
            "Select List",
            options=list(st.session_state.todo_lists.keys())
        )

        if st.button("Delete All Lists"):
            st.session_state.todo_lists = {}
            save_todo_lists(st.session_state.todo_lists)
            st.rerun()


    if selected_list and st.session_state.todo_lists:
        st.header(f"Tasks for {selected_list}")

      
        new_task = st.text_input("New Task", key=f"new_task_{selected_list}")
        if st.button("Add Task") and new_task:
            st.session_state.todo_lists[selected_list].append({
                "task": new_task,
                "completed": False,
                "created": datetime.now().isoformat()
            })
            save_todo_lists(st.session_state.todo_lists)
            st.rerun()

        if st.session_state.todo_lists[selected_list]:
            tasks = st.session_state.todo_lists[selected_list]
            for i, task in enumerate(tasks):
                col1, col2, col3 = st.columns([3, 1, 1])
                
               
                with col1:
                    display_text = f"~~{task['task']}~~" if task['completed'] else task['task']
                    st.write(display_text)
                
               
                with col2:
                    if st.button("✓", key=f"complete_{selected_list}_{i}"):
                        task['completed'] = not task['completed']
                        save_todo_lists(st.session_state.todo_lists)
                        st.rerun()
                
               
                with col3:
                    if st.button("🗑️", key=f"delete_{selected_list}_{i}"):
                        st.session_state.todo_lists[selected_list].pop(i)
                        save_todo_lists(st.session_state.todo_lists)
                        st.rerun()

      
            if st.button(f"Delete {selected_list}"):
                del st.session_state.todo_lists[selected_list]
                save_todo_lists(st.session_state.todo_lists)
                st.rerun()
        else:
            st.write("No tasks yet. Add some above!")
    elif not st.session_state.todo_lists:
        st.write("Create a list to start adding tasks!")

main()