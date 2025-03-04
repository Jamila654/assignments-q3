# type:ignore
import streamlit as st
import re
import zxcvbn
import random
import secrets
import string

class PasswordSecurityTools:
    @staticmethod
    def generate_password(length=16, include_symbols=True):
        """
        Generate a cryptographically secure password
        
        Args:
            length (int): Desired password length
            include_symbols (bool): Whether to include special characters
        
        Returns:
            str: Securely generated password
        """
        
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation if include_symbols else ''
        
        
        all_chars = lowercase + uppercase + digits + symbols
        
        
        password_chars = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits)
        ]
        
        
        if include_symbols:
            password_chars.append(secrets.choice(symbols))
        
        
        remaining_length = length - len(password_chars)
        password_chars.extend(secrets.choice(all_chars) for _ in range(remaining_length))
        
        
        random.shuffle(password_chars)
        
        return ''.join(password_chars)

    @staticmethod
    def analyze_password(password):
        """
        Analyze password strength with detailed feedback
        
        Args:
            password (str): Password to analyze
        
        Returns:
            dict: Comprehensive password strength analysis
        """
        
        if not password:
            return {
                'score': 0,
                'strength': 'No Password',
                'color': 'gray',
                'feedback': 'Please enter a password',
                'suggestions': [],
                'warnings': ''
            }
        
        
        try:
            result = zxcvbn.zxcvbn(password)
        except Exception as e:
            st.error(f"Error analyzing password: {e}")
            return {
                'score': 0,
                'strength': 'Analysis Error',
                'color': 'red',
                'feedback': 'Unable to analyze password',
                'suggestions': [],
                'warnings': ''
            }
        
        
        strength_levels = {
            0: ('Very Weak', 'darkred'),
            1: ('Weak', 'red'),
            2: ('Moderate', 'orange'),
            3: ('Strong', 'green'),
            4: ('Very Strong', 'darkgreen')
        }
        
        
        strength, color = strength_levels[result['score']]
        
        
        suggestions = result['feedback'].get('suggestions', [])
        
        
        custom_checks = []
        if len(password) < 12:
            custom_checks.append("Increase password length to at least 12 characters")
        if not re.search(r'[A-Z]', password):
            custom_checks.append("Include at least one uppercase letter")
        if not re.search(r'[a-z]', password):
            custom_checks.append("Include at least one lowercase letter")
        if not re.search(r'\d', password):
            custom_checks.append("Add at least one number")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            custom_checks.append("Use at least one special character")
        
        
        suggestions.extend(custom_checks)
        
        return {
            'score': result['score'],
            'strength': strength,
            'color': color,
            'feedback': f"{strength} Password",
            'suggestions': suggestions,
            'warnings': result['feedback'].get('warning', '')
        }

def main():
    
    st.set_page_config(
        page_title="🔒 Password Security Assistant", 
        page_icon="🔑", 
        layout="wide"
    )
    
    
    st.markdown("""
    <style>
    .main { 
        background-color: #f4f4f8; 
        padding: 2rem; 
        border-radius: 15px; 
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    st.title("🔒 Password Security Assistant")
    st.markdown("""
    Protect your digital identity with our advanced password security tools.
    Generate strong passwords and get comprehensive strength analysis.
    """)
    
    
    tab1, tab2 = st.tabs(["Password Analyzer", "Password Generator"])
    
    with tab1:
        st.header("🕵️ Password Strength Analysis")
        
        
        password = st.text_input(
            "Enter your password", 
            type="password", 
            key="analyzer_password",
            placeholder="Type a password to analyze"
        )
        
        
        if password:
            
            result = PasswordSecurityTools.analyze_password(password)
            
            
            st.progress(result['score'] * 25)
            
            
            st.markdown(f"""
            <h3 style='color:{result['color']};'>
                {result['feedback']}
            </h3>
            """, unsafe_allow_html=True)
            
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 💪 Strength Metrics")
                st.write(f"**Score:** {result['score']}/4")
                st.write(f"**Classification:** {result['strength']}")
            
            with col2:
                if result['suggestions']:
                    st.markdown("#### 🚨 Recommendations")
                    for suggestion in result['suggestions']:
                        st.markdown(f"- {suggestion}")
            
            
            if result['warnings']:
                st.warning(f"⚠️ Warning: {result['warnings']}")
    
    with tab2:
        st.header("🎲 Password Generator")
        
        
        col1, col2 = st.columns(2)
        
        with col1:
            password_length = st.slider(
                "Password Length", 
                min_value=8, 
                max_value=32, 
                value=16
            )
        
        with col2:
            include_symbols = st.checkbox("Include Special Characters", value=True)
        
        
        if st.button("Generate Secure Password", key="generate_btn"):
            generated_password = PasswordSecurityTools.generate_password(
                length=password_length, 
                include_symbols=include_symbols
            )
            st.success(f"Generated Password: {generated_password}")
            st.warning("Copy this password immediately and store it securely!")
    
    
    st.markdown("---")
    st.markdown("""
    💡 Password Security Tips:
    - Use unique passwords for each account
    - Enable two-factor authentication
    - Avoid personal information in passwords
    - Regularly update your passwords
    - Consider using a reputable password manager
    """)

if __name__ == "__main__":
    main()