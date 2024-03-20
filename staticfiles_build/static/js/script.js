const tabItems = document.querySelectorAll('.tab-item');
const tabContentItems = document.querySelectorAll('.tab-content-item');

// Select tab content item
function selectItem(e) {
	// Remove all show and border classes
	removeBorder();
	removeShow();
	// Add border to current tab item
	this.classList.add('tab-border');
	// Grab content item from DOM
	const tabContentItem = document.querySelector(`#${this.id}-content`);
	// Add show class
	tabContentItem.classList.add('show');
}


// Remove bottom borders from all tab items
function removeBorder() {
	tabItems.forEach(item => {
		item.classList.remove('tab-border');
	});
}

// Remove show class from all content items
function removeShow() {
	tabContentItems.forEach(item => {
		item.classList.remove('show');
	});
}

// Listen for tab item click
tabItems.forEach(item => {
	item.addEventListener('click', selectItem);
});

// 
// Float btn
$btnMenu.click(function() {
	var menuLink = $('.menu-link');
	var menu = $('menu');
	var close = $('.close-btn');
	var navLink = $('li a');
  
	menuLink.click(function() {
	  menu.toggleClass('active-menu');
	});
	close.click(function() {
	  menu.toggleClass('active-menu');
	});
  
	navLink.on('click', function(event) {
	  event.preventDefault();
	  var target = $(this).attr('href');
	  var top = $(target).offset().top;
	  $('html,body').animate({scrollTop: top}, 500)
	});
  });

  $(function() {
  var menuLink = $('.menu-link');
  var menu = $('menu');
  var close = $('.close-btn');
  var navLink = $('li a');

  menuLink.click(function() {
    menu.toggleClass('active-menu');
  });
  close.click(function() {
    menu.toggleClass('active-menu');
  });

  navLink.on('click', function(event) {
    event.preventDefault();
    var target = $(this).attr('href');
    var top = $(target).offset().top;
    $('html,body').animate({scrollTop: top}, 500)
  });
});


  $(function() {
	$body.toggleClass('menu-open');
  });
  
  const btnCloseBar = document.querySelector('.js-close-bar');
  const btnOpenBar = document.querySelector('.js-open-bar');
  const searchBar = document.querySelector('.searchbar');
  
  btnOpenBar.addEventListener('click', () => {
	searchBar.classList.add('bar--is-visible');
  });
  
  btnCloseBar.addEventListener('click', () => {
	searchBar.classList.remove('bar--is-visible');
  });

