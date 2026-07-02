import streamlit as st
import streamlit.components.v1 as components

# Atur halaman agar ramah mobile
st.set_page_config(layout="centered")
scratch_with_controls = """
<div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
    
    <iframe id="scratch-game" src="https://scratch.mit.edu/projects/1350792459/embed" 
            allowtransparency="true" 
            width="100%" 
            height="360" 
            frameborder="0" 
            scrolling="no" 
            allowfullscreen>
    </iframe>

    <div style="margin-top: 20px; display: flex; flex-direction: column; align-items: center; gap: 10px; width: 100%;">
        
        <button onmousedown="pressKey('ArrowUp')" onmouseup="releaseKey('ArrowUp')"
                ontouchstart="pressKey('ArrowUp')" ontouchend="releaseKey('ArrowUp')"
                style="width: 70px; height: 60px; font-size: 24px; font-weight: bold; background-color: #4CAF50; color: white; border: none; border-radius: 10px; touch-action: manipulation;">
            ▲
        </button>
        
        <div style="display: flex; gap: 40px;">
            <button onmousedown="pressKey('ArrowLeft')" onmouseup="releaseKey('ArrowLeft')"
                    ontouchstart="pressKey('ArrowLeft')" ontouchend="releaseKey('ArrowLeft')"
                    style="width: 70px; height: 60px; font-size: 24px; font-weight: bold; background-color: #2196F3; color: white; border: none; border-radius: 10px; touch-action: manipulation;">
                ◀
            </button>
            <button onmousedown="pressKey('ArrowRight')" onmouseup="releaseKey('ArrowRight')"
                    ontouchstart="pressKey('ArrowRight')" ontouchend="releaseKey('ArrowRight')"
                    style="width: 70px; height: 60px; font-size: 24px; font-weight: bold; background-color: #2196F3; color: white; border: none; border-radius: 10px; touch-action: manipulation;">
                ▶
            </button>
        </div>
    </div>
</div>

<script>
// Fungsi untuk mengirimkan sinyal keyboard ke dalam Scratch
function triggerKeyEvent(type, keyName) {
    const iframe = document.getElementById('scratch-game');
    if (iframe && iframe.contentWindow) {
        // Fokuskan ke iframe terlebih dahulu agar input diterima
        iframe.contentWindow.focus();
        
        const event = new KeyboardEvent(type, {
            key: keyName,
            code: keyName,
            bubbles: true,
            cancelable: true
        });
        iframe.contentWindow.document.dispatchEvent(event);
    }
}

function pressKey(keyName) {
    triggerKeyEvent('keydown', keyName);
}

function releaseKey(keyName) {
    triggerKeyEvent('keyup', keyName);
}
</script>
"""
components.html(scratch_with_controls, height=550)
