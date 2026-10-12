# Candidate Verfification System
from pyscript import document, display #type: ignore

def input (e):

    # clean previous output
    document.getElementById('output').innerHTML = ''
    # connect to id for last name
    last_name = document.getElementById('lname').value.title().strip()
    # connect to id for first name
    first_name = document.getElementById('fname').value.title().strip()


    # people in the jarifpa pirates for last and first name
    verified_members_lastName = ['Lao', 'Sia', 'Calaca', 'Estrada', 'Villostas', 'Alfaro']
    verfied_members_firstName = ['Liam', 'Agatha', ' Mohammad', 'Lara', 'Devon', 'Athena']

    # check list from the input
    verify_lname = last_name in verified_members_lastName
    verify_fname = first_name in verfied_members_firstName

    # response if true or false
    response = ('I apologies, you are NOT a member of the J.A.R.I.F.P.A', f'Welcome {first_name} {last_name}, you are a member of the J.A.R.I.F.P.A. Pirates')
    # print output on website
    display(response[verify_lname], target='output')