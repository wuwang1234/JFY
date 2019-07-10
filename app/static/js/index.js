$(document).ready(function(){
	$.ajax({
		type:"get",
		url:"/api/search/content/",
		async:true,
		dataType:'json',
		success:function(result){
			if($.isEmptyObject(result)){
				alert('暂无记录！')
			}
			else{
				console.log(typeof(result))
				console.log()
				for(var i=0,i<result.length,i++){
				$(".arctiles_title").html(result[0].title)
				$(".arctile_type").html(result[0].classify)
				var author = result[0].author
				if ($.isEmptyObject(author)){
					author = '匿名'
				}
				$(".arctile_author").html(author)
				$(".arctile_update").html(result[0].date)
				}

			}
	
		}
	});
});

