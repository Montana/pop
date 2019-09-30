def test_cases(number):
    return testCases[number]
testCases = [
    #[severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Main page, when user click "Sing in" button, without providing mandatorty fields'],
    ['Blocker', 'when user login with a valid user, he should see Home Page'],
    ['Blocker', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
    ['Major', 'To check the pointing of server by using demo account credentials'],
    ['Blocker',  'when user clicks on unregister button and accepts the alert, it should regirect to login page'],
    ['Blocker',  'when user clicks on unregister button and cancel the alert, it should remain to employee page'],
    ['Blocker',  'In employee login page, when user clicks on any emoployee and provide valid pin, he/she should able to login'],
    ['Blocker',  'In employee login page, when user clicks on any emoployee and provide invalid pin, he/she should see an error message'],
    ['Blocker',  'To click on drop of select resturant']