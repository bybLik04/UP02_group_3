
var toggleButton2 = document.getElementById('toggleButton2');
var hiddenTextContainer2 = document.getElementById('hiddenTextContainer2');
hiddenText2 = document.getElementById('hiddenText2');

toggleButton2.addEventListener('click', function () {
    if (hiddenTextContainer2.style.height === '0px') {
        hiddenTextContainer2.style.height = hiddenText2.offsetHeight + 'px';
        hiddenText2.style.opacity = '1';
    } else {
        hiddenTextContainer2.style.height = '0px';
        hiddenText.style2.opacity = '0';
    }
});