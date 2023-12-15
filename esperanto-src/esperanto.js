function translate(text){
    var latin = ['CX', 'GX', 'HX', 'JX', 'SX', 'UX', 'cx', 'gx', 'hx', 'jx', 'sx', 'ux',
                    'Cx', 'Gx', 'Hx', 'Jx', 'Sx', 'Ux'];
    var esperanto = ['Ĉ', 'Ĝ', 'Ĥ', 'Ĵ', 'Ŝ', 'Ŭ', 'ĉ', 'ĝ', 'ĥ', 'ĵ', 'ŝ', 'ŭ'];
    txtMessage.value = "";
    for (let i = 0; i < text.length; i++){
        let index = latin.indexOf(text[i] + text[i + 1]);
        if (index === -1){
            txtMessage.value += text[i];
            continue;
        }
        if (index > 11){ 
            txtMessage.value += esperanto[index - 12];
            i++;
            continue;
        }
        txtMessage.value += esperanto[index];
        i++;
    }
}
const btnTranslate = document.querySelector("#translate")
const txtMessage = document.querySelector("#message")

btnTranslate.addEventListener("click",() => {
    translate(txtMessage.value)
})