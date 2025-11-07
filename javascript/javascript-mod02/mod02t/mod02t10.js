// Write a voting program as described below for small-scale meeting use. (8p)
// The program asks for the number of candidates.
// Then the program asks for the names of the candidates: Name for candidate 1
// Store the candidates names and initial vote count in objects like this:

// === VOTING PROGRAM (Pure JavaScript) ===

// 1. Number of candidates
let candidateCount = parseInt(prompt("Enter the number of candidates:"));
while (isNaN(candidateCount) || candidateCount <= 0) {
    candidateCount = parseInt(prompt("Invalid. Enter a positive number of candidates:"));
}

// 2. Create candidates array with objects
let candidates = [];
for (let i = 0; i < candidateCount; i++) {
    let name = prompt(`Name for candidate ${i + 1}:`).trim();
    while (!name) {
        name = prompt(`Name cannot be empty. Enter name for candidate ${i + 1}:`).trim();
    }
    candidates.push({ name: name, votes: 0 });
}

// 3. Number of voters
let voterCount = parseInt(prompt("Enter the number of voters:"));
while (isNaN(voterCount) || voterCount <= 0) {
    voterCount = parseInt(prompt("Invalid. Enter a positive number of voters:"));
}

// 4. Voting loop
for (let i = 0; i < voterCount; i++) {
    let vote = prompt(`Voter ${i + 1}, enter candidate name to vote for:`).trim();

    // Empty vote = skip
    if (vote === "") {
        continue;
    }

    // Find candidate (case-insensitive)
    let voted = false;
    for (let cand of candidates) {
        if (cand.name.toLowerCase() === vote.toLowerCase()) {
            cand.votes++;
            voted = true;
            break;
        }
    }

    if (!voted) {
        alert(`No candidate named "${vote}". Vote ignored.`);
    }
}

// 5. Sort by votes (descending)
candidates.sort((a, b) => b.votes - a.votes);

// 6. Winner
let winner = candidates[0];
let winnerText = `The winner is ${winner.name} with ${winner.votes} vote${winner.votes !== 1 ? 's' : ''}.`;

// 7. Print results to console
console.log(winnerText);
console.log("results:");
for (let cand of candidates) {
    console.log(`${cand.name}: ${cand.votes} vote${cand.votes !== 1 ? 's' : ''}`);
}