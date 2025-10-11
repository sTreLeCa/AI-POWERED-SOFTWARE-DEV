const API_KEY = 'key'; // Replace with your actual Gemini API key
const copyBtn = document.getElementById('copy-btn');

copyBtn.addEventListener('click', () => {
    const outputText = document.getElementById('output').textContent;
    navigator.clipboard.writeText(outputText).then(() => {
        copyBtn.textContent = 'Copied!';
        setTimeout(() => {
            copyBtn.textContent = 'Copy';
        }, 2000);
    }).catch(err => console.error('Failed to copy text: ', err));
});

function calculateCost(inputTokens, outputTokens) {
    const INPUT_COST_PER_1K = 0.00025;
    const OUTPUT_COST_PER_1K = 0.0005;
    const inputCost = (inputTokens / 1000) * INPUT_COST_PER_1K;
    const outputCost = (outputTokens / 1000) * OUTPUT_COST_PER_1K;
    return {
        input: inputCost,
        output: outputCost,
        total: inputCost + outputCost
    };
}

async function fetchWithRetry(url, options, maxRetries = 3) {
    for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
            const response = await fetch(url, options);
            if (!response.ok) throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            return response;
        } catch (error) {
            console.error(`Attempt ${attempt + 1} failed:`, error.message);
            if (attempt === maxRetries - 1) throw error;
            await new Promise(resolve => setTimeout(resolve, Math.pow(2, attempt) * 1000));
        }
    }
}

async function generateTextStreaming() {
    const prompt = document.getElementById('promptInput').value;
    const outputDiv = document.getElementById('output');
    const inputTokensEl = document.getElementById('input-tokens');
    const outputTokensEl = document.getElementById('output-tokens');
    const totalCostEl = document.getElementById('total-cost');

    if (!prompt.trim()) { alert('Please enter a prompt!'); return; }

    outputDiv.textContent = '';
    inputTokensEl.textContent = '...';
    outputTokensEl.textContent = '...';
    totalCostEl.textContent = '...';
    copyBtn.disabled = true;
    copyBtn.textContent = 'Copy';

    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key=${API_KEY}`;
    const options = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
    };

    try {
        const response = await fetchWithRetry(url, options);
        const data = await response.json();

        const fullText = data.candidates[0].content.parts[0].text;
        let i = 0;

        const words = fullText.split(/(\s+)/);
        const interval = setInterval(() => {
            if (i < words.length) {
                outputDiv.textContent += words[i];
                i++;
            } else {
                clearInterval(interval);
            }
        }, 30);

        const usage = data.usageMetadata || {};
        const inputTokens = usage.promptTokenCount || 0;
        const outputTokens = usage.candidatesTokenCount || 0;
        const cost = calculateCost(inputTokens, outputTokens);

        setTimeout(() => {
            inputTokensEl.textContent = inputTokens;
            outputTokensEl.textContent = outputTokens;
            totalCostEl.textContent = `$${cost.total.toFixed(6)}`;
            copyBtn.disabled = false;
        }, words.length * 30 + 100);

    } catch (error) {
        outputDiv.textContent = 'Error: ' + error.message;
        inputTokensEl.textContent = '0';
        outputTokensEl.textContent = '0';
        totalCostEl.textContent = '$0.000000';
        copyBtn.disabled = false;
    }
}

window.generateTextStreaming = generateTextStreaming;

function initializeFooter() {
    const footerElement = document.getElementById('footer-content');
    const userEmail = "pluzhnikovi.aleksand@kiu.edu.ge";
    const currentDate = new Date();
    const formattedDate = currentDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
    const currentYear = currentDate.getFullYear();
    footerElement.textContent = `© ${currentYear} ${userEmail} - ${formattedDate}`;
}

document.addEventListener('DOMContentLoaded', initializeFooter);
