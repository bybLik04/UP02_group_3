$(document).ready(function () {
    $('.content picture img').hide(); // ������� �������� �������� 
    $('.content picture img').css({ opacity: 0, marginTop: '20px' }); // ������������� ��������� �����

    $('.content picture img').slideDown(1000).animate({ opacity: 1 }, 1000); // ��������� �������� ��� ������ ���� � �������� ���������
});
