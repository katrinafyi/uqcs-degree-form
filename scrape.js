// should be executed in console context of this page:
// https://my.uq.edu.au/programs-courses/browse.html?level=ugpg

(function() {
    const $$ = x => Array.from(document.querySelectorAll(x));

    const programs = [];
    // for each program
    $$('a[href^="/programs-courses/program.html?acad_prog="]')
    .map(a => {
        const prog = a.textContent.trim();
        const program = {
            name: prog,
            type: null,
            majors: [],
        };
        programs.push(program);
        const majors = program.majors;

        let el = a.parentNode.parentNode; // get tr containing this a
        
        while (true) {
            if (!el) break; // reached end of this letter's table.
            const title = el.querySelector('.title').textContent.trim();
            if (title && title !== prog) break; // reached next program

            const major = el.querySelector('.plan').textContent.trim();

            if (majors.indexOf(major) == -1)
                majors.push(major);

            program.type = el.querySelector('.type').textContent.trim();
            el = el.nextElementSibling;
        }
    });
    
    console.log(programs);
    console.log(JSON.stringify(programs, undefined, 0));
})();