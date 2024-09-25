	
	if( 'ontouchstart' in window ){ var click = 'touchstart'; }
	else { var click = 'click'; }


	$('div.burger').on(click, function(){

			if( !$(this).hasClass('open') ){ openMenu(); } 
			else { closeMenu(); }

	});
		

	function openMenu(){
		document.getElementById('openContactModalBtn').style.display ='none';
		$('div.circle').addClass('expand');
					
		$('div.burger').addClass('open');	
		$('div.x, div.y, div.z').addClass('collapse');
		$('.menu li').addClass('animate');
		
		setTimeout(function(){ 
			$('div.y').hide(); 
			$('div.x').addClass('rotate30'); 
			$('div.z').addClass('rotate150'); 
		}, 70);
		setTimeout(function(){
			$('div.x').addClass('rotate45'); 
			$('div.z').addClass('rotate135');  
		}, 120);
		
		

	}
	
	function closeMenu(){
		$('div.burger').removeClass('open');	
		$('div.x').removeClass('rotate45').addClass('rotate30'); 
		$('div.z').removeClass('rotate135').addClass('rotate150');				
		$('div.circle').removeClass('expand');
		$('.menu li').removeClass('animate');
		
		setTimeout(function(){ 			
			$('div.x').removeClass('rotate30'); 
			$('div.z').removeClass('rotate150'); 			
		}, 50);
		setTimeout(function(){
			$('div.y').show(); 
			$('div.x, div.y, div.z').removeClass('collapse');
		}, 70);
        document.getElementById('openContactModalBtn').style.display ='inline-block';

		
	}