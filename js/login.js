function login (u,p) {
	$.get('./cgi-bin/LLajax.py?act=login&f=1&u='+u+'&p='+p, function(data, status) {
		if (data == 1) {
			$.notify('Loged In ...', "success");
			window.location.href = "./cgi-bin/LLcore.py";
		} else {
			$.notify(data);
		}
	});
}

$(document).ready( function () {
	$('body').on('click','#do-login',function(){
		var u=$("#u").val();
		var p=$("#p").val();
		Cookies.set('u', u);
		Cookies.set('p', p);
		login (u,p);
	});
});

login (Cookies.get('u', u),Cookies.get('p', p));

console.log(Cookies.get('u', u),Cookies.get('p', p));