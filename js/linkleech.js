function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  return !!pattern.test(str);
}

function queue () {
	sleep(350);
	$.get('./LLajax.py?act=list&list=progress', function(data, status) {
		var resp = JSON.parse (data);
		var replistd;
		for(var k in resp) {
			var filename = resp[k][0].replace(/^.*[\\\/]/, '');
			let url= '<a href="'+resp[k][0]+'" target="_blank"><img src="http://www.google.com/s2/favicons?domain='+resp[k][0]+'" role="button" data-toggle="popover" title="Sourc Link" data-content="'+resp[k][0]+'" > '+filename+' </a>';
			let path= '<a href="../'+resp[k][1]+filename+'" target="_blank"><img src="http://www.google.com/s2/favicons?domain=download.cnet.com" role="button" data-toggle="popover" title="New Link" data-content="../files'+resp[k][1]+filename+'" ></a>';
			let type=(resp[k][3]==1)?'PY GET':'MS CURL';
			let status='<kbd class="bg-white green border border-success">Downloding <div class="spinner-grow text-success" style="width: 1rem; height: 1rem;" role="status"> <span class="sr-only">Loading...</span></div></kbd>';
			replistd += '<tr><td class="text-left">'+url+'</td><td>'+path+'</td><td>'+resp[k][2]+'</td><td>'+type+'</td><td><div class="btn-group">'+status+'</div></td></tr>';
		}
		$.get('./LLajax.py?act=list&list=queue', function(data, status) {
			var resp = JSON.parse (data);
			var replistq;
			for(var k in resp) {
				var filename = resp[k][0].replace(/^.*[\\\/]/, '');
				let url= '<a href="'+resp[k][0]+'" target="_blank"><img src="http://www.google.com/s2/favicons?domain='+resp[k][0]+'" role="button" data-toggle="popover" title="Sourc Link" data-content="'+resp[k][0]+'" > '+filename+' </a>';
				let path= '<a href="../files'+resp[k][1]+filename+'" target="_blank"><img src="http://www.google.com/s2/favicons?domain=download.cnet.com" role="button" data-toggle="popover" title="New Link" data-content="../files'+resp[k][1]+filename+'" ></a>';
				let type=(resp[k][3]==1)?'PY GET':'MS CURL';
				let status='<kbd class="bg-warning">On Hold</kbd>';
				let delkey='<button id="do-delete" class="btn btn-sm btn-danger k-del" data-tu="'+resp[k][0]+'" type="button"><strong>X</strong></button>';
				replistq += '<tr><td class="text-left">'+url+'</td><td>'+path+'</td><td>'+resp[k][2]+'</td><td>'+type+'</td><td><div class="btn-group">'+status+delkey+'</div></td></tr>';
			}
			$( "#queue" ).html(replistd+replistq);		   
		});
	});
	$.get('./LLajax.py?act=list&list=result', function(data, status) {
		var resp = JSON.parse (data);
		var result;
		for(var k in resp) {
			var filename = resp[k][0].replace(/^.*[\\\/]/, '');
			let url= '<a href="'+resp[k][0]+'" target="_blank"><img src="http://www.google.com/s2/favicons?domain='+resp[k][0]+'" role="button" data-toggle="popover" title="Sourc Link" data-content="'+resp[k][0]+'" > '+filename+' </a>';
			let path= '<a href="../'+resp[k][1]+'" target="_blank"><img src="http://www.google.com/s2/favicons?domain=download.cnet.com" role="button" data-toggle="popover" title="New Link" data-content="../'+resp[k][1]+'" ></a>';
			let status='<kbd class="bg-green">Downloded</kbd>';
			result += '<tr><td class="text-left">'+url+'</td><td>'+path+'</td><td><div class="btn-group">'+status+'</div></td></tr>';
		}
		$( "#result" ).html(result);		   
	});
	$.get('./LLajax.py?act=list&list=errors', function(data, status) {
		var resp = JSON.parse (data);
		var errors;
		for(var k in resp) {
			var filename = resp[k][0].replace(/^.*[\\\/]/, '');
			let url= '<a href="'+resp[k][0]+'" target="_blank"><img src="http://www.google.com/s2/favicons?domain='+resp[k][0]+'" role="button" data-toggle="popover" title="Sourc Link" data-content="'+resp[k][0]+'" > '+filename+' </a>';
			let type=(resp[k][3]==1)?'PY GET':'MS CURL';
			let status='<kbd class="bg-dorange">Error</kbd>';
			errors += '<tr><td class="text-left">'+url+'</td><td>'+resp[k][2]+'</td><td>'+type+'</td><td><div class="btn-group">'+status+'</div></td></tr>';
		}
		$( "#errors" ).html(errors);
		$("#result, #errors").each(function(elem,index){
			var arr = $.makeArray($("tr",this).detach());
			arr.reverse();
			$(this).append(arr);
		});
	});
}

$(document).ajaxComplete(function() {
	$('[data-toggle="popover"]').popover({ trigger: "hover" });
});

$(document).ready( function () {
	
	$('body').on('click','#do-logout',function(){
		Cookies.remove('u');
		Cookies.remove('p');
		$.notify('Loged Out ...', "success");
		window.location.href = "../login.htm";
	});
	
	$('body').on('click','#do-addQueue',function(){
		var lines = $('#url').val().split('\n');
		for(var i = 0;i < lines.length;i++) {
			sleep(150);
			var url=lines[i];
			if (validURL(url)) {
				var path=$("#path").val();
				var conc=$("#conc").val();
				var type=$("#type").val();
				var string='&url='+url+'&path='+path+'&conc='+conc+'&type='+type;
				$.get('./LLajax.py?act=addQueue'+string, function(data, status) {
					if (data == 1) {
						$.notify('Files Added to Queue', "success");
					} else {
						$.notify(data);
					}
				});
			} else {
				$.notify(url+' Is not URL !', "danger");
			}
		}
		queue();
	});

	$('body').on('click','#do-delete',function() {
		let tu = $(this).data('tu');
		let string = '&tu='+tu;
			$.get('./LLajax.py?act=delQueue'+string+'&0', function(data, status) {
				if (data == 0) {
					$.notify(data + ' Files removed');
				} else {
					$.notify(data + ' Files removed from queue' , "success");
					queue();
				}
			});
	});

	$('body').on('click','.do-clear',function() {
		let list = $(this).data('list');
		let string = '?act=clear&list='+list;
			$.get('./LLajax.py'+string+'&0', function(data, status) {
				if (data == 1) {
					$.notify(list +' Logs Cleared', "success");
					$( "#"+list ).html('');
				} else {
					$.notify('Error !');
				}
			});
	});
	
	window.setInterval(function(){
		queue();
	}, 3300);
	
	queue();
});