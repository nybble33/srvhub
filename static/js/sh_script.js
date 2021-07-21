
function resp_format(json_string){
    if (json_string.error){
        return 'Error: '+json_string.error
    } else {
        json_str = JSON.parse(json_string);
        resp_html = '<ul>';
        resp_html+= '<li style="color: #00f">Token of your request: '+json_str.token+'</li>';
        resp_html+= '<li>Response: '+json_str.response+'</li>';
        resp_html+= '</ul>';
        return resp_html
    }
}

function get_form_ready(){
    $("#var_1_form").on("submit", function(event){
        event.preventDefault();
        url_value = $('input[name="url"]').val();
        token_value = $('input[name="token"]').val();
        $.ajax({
            url: 'http://serv-hub.nybble.ru/var-1/',
            type: 'GET',
            data_type: 'json',
            data: `url=${url_value}&token=${token_value}`,
            success: function(data){
                response = JSON.stringify(data);
                response_text = resp_format(response);
                resp_html = `<div>${response_text}</div>`;
                $('#resp').html(resp_html);
            },
            error: function (jqXHR, exception){
                alert(jqXHR.status);
            },
        })
    })
}

$(document).ready(function(){
    get_form_ready();
})
