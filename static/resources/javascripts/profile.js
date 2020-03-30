function hideButton() {
    let textarea = document.getElementById('textArea');
    let button = document.getElementById('button');
    let submit = document.getElementById('submit');
    textarea.style.display ='inline-block';
    button.style.display = 'none';
    submit.style.display = 'inline-block';
}

function editteacherId() {
    let input = document.getElementById('teacherId')
    let button = document.getElementById('teacherIdbutton')
    let teacherID = document.getElementById('teacherID')
    

    input.style.display = 'inline'
    button.style.display = 'inline'
    
}

function editProgilePhoto(){
    let form = document.getElementById('photoForm')
    let button = document.getElementById('photoFormButton')

    form.style.display = 'inline'
    button.style.display = 'inline'
}