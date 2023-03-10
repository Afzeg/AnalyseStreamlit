import streamlit as st
import base64
from streamlit.components.v1 import html
from PATHS import NAVBAR_PATHS

def inject_custom_css():
    with open('src/assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def navbar_component():
    
    component = rf'''
            <nav class="container navbar" id="navbar">
                <label for="toggle">☰</label>
                <input type="checkbox" id="toggle">
                <ul class="navlist">
                    <a class="navitem" href="/?nav=%2Fhome">ACCUEIL</a>
                    <a class="navitem" href="/?nav=%2Fdataset">JEU DE DONNEES</a>
                    <a class="navitem" href="/?nav=%2Fanalysis">ANALYSE</a>
                    <a class="navitem" href="/?nav=%2Fconclusion">CONCLUSION</a>
                    <a class="navitem" href="/?nav=%2Flogout">DECONNEXION</a>
                </ul>
            </nav>
            '''
    st.markdown(component, unsafe_allow_html=True)
    
    js = '''
    <script>
        // navbar elements
        var navigationTabs = window.parent.document.getElementsByClassName("navitem");
        var cleanNavbar = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }
        
        for (var i = 0; i < navigationTabs.length; i++) {
            cleanNavbar(navigationTabs[i]);
        }
        
        // Dropdown hide / show
        var dropdown = window.parent.document.getElementById("settingsDropDown");
        dropdown.onclick = function() {
            var dropWindow = window.parent.document.getElementById("myDropdown");
            if (dropWindow.style.visibility == "hidden"){
                dropWindow.style.visibility = "visible";
            }else{
                dropWindow.style.visibility = "hidden";
            }
        };
        
        var settingsNavs = window.parent.document.getElementsByClassName("settingsNav");
        var cleanSettings = function(navigation_element) {
            navigation_element.removeAttribute('target')
        }
        
        for (var i = 0; i < settingsNavs.length; i++) {
            cleanSettings(settingsNavs[i]);
        }
    </script>
    '''
    html(js)