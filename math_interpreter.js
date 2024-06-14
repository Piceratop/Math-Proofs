const mathVariables = {};
const keywords = new Set(["=", "let", "{", "}"]);

function displayError(text) {
    console.log(text);
    process.exit(1);
}

function validateMinTokens(tokens, keyword, required) {
    if (tokens.length < required) {
        displayError(`Syntax error: ${keyword} requires at least ${required - 1} arguments.`)
    }
}

function validateNonkeyword(token) {
    if (keywords.has(token)) {
        displayError(`Syntax error: ${token} is a keyword.`)
    }
}

function validateKeyword(token, keyword) {
    if (token !== keyword) {
        displayError(`Syntax error: ${token} is not a ${keyword}.`)
    }
}

const fs = require('fs');
const file = fs.readFileSync('test.mthc', 'utf8').split('\n');
file.forEach((codeLines) => {
    const tokens = codeLines.split(/\s+/);
    switch (tokens[0]) {
        case "let":
            validateNonkeyword(tokens[1]);
            if (tokens.length == 2) {
                mathVariables[tokens[1]] = {
                    "value": undefined,
                    "type": "any"
                }
            } else {
                validateKeyword(tokens[2], "=");
                bracketStack = [];
                currV = new Set();
                
            }
            break;
        default:
            break;
    }
})

console.log(mathVariables);