function highlightCode(code) {
        const keywords = /\b(function|let|const|if|else|return)\b/g;
        const strings = /(".*?"|'.*?')/g;
        const numbers = /\b\d+\b/g;
        return code
                .replace(keywords, '<span class="keyword">$&</span>')
                .replace(strings, '<span class="string">$&</span>')
                .replace(numbers, '<span class="number">$&</span>');
}
const code = `
        function add(a, b) {
        if (a > 0) {
                return a + b;
        } else {
                return "invalid";
        }
}`;
document.body.innerHTML = `<pre>${highlightCode(code)}</pre>`;
const style = document.createElement('style');
style.textContent = `
        .keyword { color: blue; font-weight: bold; }
        .string { color: green; }
        .number { color: red; }
`;
document.head.appendChild(style);
