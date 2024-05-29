const math_variables = {};
const keywords = new Set(["=", "let", "{", "}"]);

function display_error(text) {
    console.log(text);
    process.exit(1);
}

function validate_min_tokens(tokens, keyword, required) {
    if (tokens.length < required) {
        display_error(`Syntax error: ${keyword} requires at least ${required - 1} arguments.`)
    }
}

function validate_nonkeyword(token) {
    if (keywords.has(token)) {
        display_error(`Syntax error: ${token} is a keyword.`)
    }
}


console.log(math_variables);