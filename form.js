fetch('ugpg.json')
.then(x => x.json())
.then(x => {
    progInput = new Awesomplete('#program', {
        minChars: 1,
        list: Object.keys(x),
        autoFirst: true,
    });

    const majorInput = new Awesomplete('#major', {
        minChars: 1,
        autoFirst: true,
        list: []
    });

    progInput.input.addEventListener('awesomplete-selectcomplete', ({text}) => {
        document.getElementById('program-display').textContent = text.value;
        majorInput.list = x[text.value];
    });

    majorInput.input.addEventListener('awesomplete-selectcomplete', ({text}) => {
        document.getElementById('major-display').textContent = text.value;
        document.getElementById('display').style.display = '';
    });
});


