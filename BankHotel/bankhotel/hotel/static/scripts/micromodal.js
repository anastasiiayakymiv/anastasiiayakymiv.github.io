MicroModal.init({
    onShow: modal => console.info(`${modal.id} is shown`), 
    onClose: modal => console.info(`${modal.id} is hidden`), 
    openTrigger: 'data-custom-open',
    closeTrigger: 'data-custom-close',
    disableScroll: true, 
    disableFocus: false, 
    awaitCloseAnimation: false, 
    debugMode: true 
  });

var button = document.querySelector('.btn');
  button.addEventListener('click', function(){
    MicroModal.show('modal-1');    
});
var button2 = document.querySelector('.bookroom-icon');
  button2.addEventListener('click', function(){
    MicroModal.show('modal-1');    
});