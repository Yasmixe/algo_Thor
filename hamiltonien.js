function addInputFields() {
    var nb = document.getElementById('nbTasks').value;

    // Clear previous input fields
    document.getElementById('inputFields').innerHTML = '';

    // Add input fields for tasks and their durations
    for (var i = 1; i <= nb; i++) {
        var label = document.createElement('label');
        label.for = 'taskDuration' + i;
        label.textContent = 'Duration of Task ' + i + ':';

        var input = document.createElement('input');
        input.type = 'number';
        input.id = 'taskDuration' + i;

        document.getElementById('inputFields').appendChild(label);
        document.getElementById('inputFields').appendChild(input);
        document.getElementById('inputFields').appendChild(document.createElement('br'));
    }
    for (var i = 1; i <= nb; i++) {
        for (var j = 1; j <= nb; j++) {
            if (j !== i) {
                var label = document.createElement('label');
                label.for = 'transition_' + i + '_' + j;
                label.textContent = 'Transition from Task ' + i + ' to Task ' + j + ':';

                var input = document.createElement('input');
                input.type = 'number';
                input.id = 'transition_' + i + '_' + j;
                input.name = 'transition_' + i + '_' + j; // Added name attribute

                document.getElementById('inputFields').appendChild(label);
                document.getElementById('inputFields').appendChild(input);
                document.getElementById('inputFields').appendChild(document.createElement('br'));
            }
        }
    }
}

function calculateHamiltonianPath() {
    // Get the number of tasks
    var nb = parseInt(document.getElementById('nbTasks').value);

    // Get the durations of each task
    var tempsExec = [];
    for (var i = 1; i <= nb; i++) {
        tempsExec.push(parseInt(document.getElementById('taskDuration' + i).value));
    }

    // Get the transition matrix
    var rows = [];
    for (var i = 1; i <= nb; i++) {
        var col = [];
        for (var j = 1; j <= nb; j++) {
            if (j === i) {
                col.push(0);
            } else {
                var x = parseInt(document.getElementById('transition_' + i + '_' + j).value);
                col.push(x);
            }
        }
        rows.push(col);
    }
    console.log(rows);

    // Initialize variables for Hamiltonian path calculation
    var start = (rows.length > 0 && rows[0].length > 0) ? Math.min(...rows[0].filter(x => x !== 0)) : -1;
    var index = (rows.length > 0 && rows[0].length > 0) ? rows[0].indexOf(start) : -1;
    var cheminHamilton = (start !== -1) ? [start] : [];
    var ordonnancement = (start !== -1) ? [1, index + 1] : [];

    // Calculate Hamiltonian path
    for (var j = 1; j < nb - 1 && start !== -1 && index !== -1; j++) {
        var next = Math.min(...rows[index].map((x, i) => (x !== 0 && !ordonnancement.includes(i + 1)) ? x : Infinity));
        index = rows[index].indexOf(next);
        cheminHamilton.push(next);
        ordonnancement.push(index + 1);
    }

    var tailleChemin = cheminHamilton.reduce((acc, val) => acc + val, 0);

    // Find the optimal Hamiltonian path
    for (var i = 1; i < nb && start !== -1 && index !== -1; i++) {
        start = (rows.length > i && rows[i].length > 0) ? Math.min(...rows[i].filter(x => x !== 0)) : -1;
        index = (rows.length > i && rows[i].length > 0) ? rows[i].indexOf(start) : -1;
        var cheminHamiltonTest = (start !== -1) ? [start] : [];
        var ordonnancementTest = (start !== -1) ? [i + 1, index + 1] : [];
        for (var j = 1; j < nb - 1 && start !== -1 && index !== -1; j++) {
            var next = Math.min(...rows[index].map((x, i) => (x !== 0 && !ordonnancementTest.includes(i + 1)) ? x : Infinity));
            index = rows[index].indexOf(next);
            cheminHamiltonTest.push(next);
            ordonnancementTest.push(index + 1);
        }
        var taille = cheminHamiltonTest.reduce((acc, val) => acc + val, 0);
        if (taille < tailleChemin) {
            tailleChemin = taille;
            cheminHamilton = cheminHamiltonTest;
            ordonnancement = ordonnancementTest;
        }
    }

    console.log("L'ordonnancement est :", ordonnancement);
    console.log("Cmax= ", tailleChemin + tempsExec.reduce((acc, val) => acc + val, 0));
    // Display results
    var ordonnancementResult = document.getElementById('ordonnancementResult');
    var cmaxResult = document.getElementById('cmaxResult');
    var resultsContainer = document.getElementById('results');

    if (ordonnancementResult && cmaxResult && resultsContainer) {
        ordonnancementResult.textContent = "L'ordonnancement est : " + JSON.stringify(ordonnancement);
        cmaxResult.textContent = "Cmax= " + (tailleChemin + tempsExec.reduce((acc, val) => acc + val, 0));

        // Show the results container
        resultsContainer.classList.remove('hidden');
    }
}


// Call the function to start the calculation
calculateHamiltonianPath();
