document.addEventListener('DOMContentLoaded', function () {
    const submitBtn = document.getElementById('submitBtn');
    const fileInput = document.getElementById('codefile');
    const resultDiv = document.getElementById('result');

    submitBtn.addEventListener('click', async function () {
        const file = fileInput.files[0];

        if (!file) {
            resultDiv.innerHTML = "<p style='color:red;'>Please select a Python file.</p>";
            return;
        }

        const formData = new FormData();
        formData.append('codefile', file);

        resultDiv.innerHTML =   '<div class="overlay"></div>\n' +
                                '<div class="loader"></div>';

        try {
            const response = await fetch('/solid', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const html = await response.text();
            resultDiv.innerHTML = "<h2>Result:</h2>" + html;
        } catch (err) {
            resultDiv.innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
        }
    });
});
