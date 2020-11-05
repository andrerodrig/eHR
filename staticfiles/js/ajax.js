$('.prevented').click((event) => {
    event.preventDefault()
})

function hasUsedOvertime(id) {
    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (result) {
            console.log(result);
            $('#mensagem').text(result.mensagem);
            $('#horas-atualizadas').text(result.horas);

        }
    });
}

function hasNotUsedOvertime(id) {
    let token = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        type: 'POST',
        url: '/horas-extras/nao-utilizou-hora-extra/' + id,
        data: {
            csrfmiddlewaretoken: token
        },
        success: (result) => {
            console.log(result);
            $('#mensagem').text(result.mensagem);
            $('#horas-atualizadas').text(result.horas);
        }
    });
}