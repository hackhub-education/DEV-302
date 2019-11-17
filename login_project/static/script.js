function loginCheck(){
	const username = $('#username').val();
	const password = $('#password').val();
	
	console.log("username = ", username);
	console.log("password = ", password);
	if(username == ""){
		$('#username_hint').fadeIn(2000);
		// $('#username_hint').removeClass('hidden');
	}

	// ajax

	// json
	const response = {"status":"success", "data":"..."};
	// const response = {"status":"fail", "data":"...", "message":""};
	if (response.status == 'success'){
		//redirect user to the application
	}
	else if(response.status == 'fail'){
		alert(response.message);
	}
	else{
		alert("system, contact system admin.")
	}
}



$(document).ready(function(){
	$('#submit2').click(function(e){
		e.preventDefault();
		loginCheck();
	});
	$('#submit3').click(function(){
		loginCheck();
	});

	// $('#submit3').click(()=> loginCheck());

});