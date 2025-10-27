function ask(message, _default="", hint="Please enter a valid response.") {
    let response = prompt(message, _default)?.trim();
    if (!response) {
    alert(hint);
    return ask(message);
    }
    return response;
}