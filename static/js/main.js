document.addEventListener('DOMContentLoaded', () => {
    const editor = document.getElementById('editor');
    const toneSelect = document.getElementById('toneSelect');
    const generatedText = document.getElementById('generated-text');
    const newBtn = document.getElementById('newBtn');
    const openBtn = document.getElementById('openBtn');
    const saveBtn = document.getElementById('saveBtn');
    const fileInput = document.getElementById('fileInput');

    let currentTone = toneSelect.value;
    let lastGeneratedText = '';

    // Handle tone selection
    toneSelect.addEventListener('change', async () => {
        currentTone = toneSelect.value;
        if (editor.value.trim()) {
            await generateText();
        }
    });

    // Handle file operations
    newBtn.addEventListener('click', () => {
        editor.value = '';
        generatedText.textContent = '';
    });

    openBtn.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                editor.value = e.target.result;
            };
            reader.readAsText(file);
        }
    });

    saveBtn.addEventListener('click', () => {
        const text = editor.value;
        const blob = new Blob([text], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'document.txt';
        a.click();
        window.URL.revokeObjectURL(url);
    });

    // Generate text using AI
    async function generateText() {
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: editor.value,
                    tone: currentTone
                })
            });

            const data = await response.json();

            if (data.success) {
                lastGeneratedText = data.generated_text;
                generatedText.textContent = lastGeneratedText;
            } else {
                generatedText.textContent = 'Error: ' + data.error;
            }
        } catch (error) {
            generatedText.textContent = 'Error: Failed to generate text';
            console.error('Error:', error);
        }
    }

    // Add keyboard shortcut for generating text (Ctrl+Enter)
    editor.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'Enter') {
            generateText();
        }
    });
}); 