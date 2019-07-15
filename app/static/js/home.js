$(document).ready(function(){
	$.ajax({
		type:"get",
		url:"/api/search/content/",
		async:true,
		dataType:'json',
		success:function(result){
			var li_content = $('.arctile_ul').html()
			console.log(li_content)
			var html_content = ''
			ul = $('.arctile_ul')
			if($.isEmptyObject(result)){
				ul.html(html_content)
				alert('暂无记录！')
			}
			else{
				console.log(typeof(result))
				console.log()
				for(var i=0;i<result.length;i++){
					html_content = $('.arctile_ul').html()
					if(i>0){
						html_content =html_content +li_content
					}				
					ul.html(html_content)
					$(".arctiles_title").eq(i).html(result[i].title)
					$(".arctile_type").eq(i).html(result[i].classify)
					$(".arctile_author").eq(i).html(result[i].author)
					$(".arctile_update").eq(i).html(result[i].date)
				}

			}
	
		}
	});
});

