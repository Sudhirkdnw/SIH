let posts = [];

// Function to handle post submission
document.getElementById('submitPost').addEventListener('click', () => {
    const username = document.getElementById('username').value;
    const postText = document.getElementById('postText').value;
    const imageUpload = document.getElementById('imageUpload').files[0];

    if (username && postText) {
        const reader = new FileReader();
        reader.onload = function () {
            const post = {
                username,
                postText,
                image: reader.result,
                comments: []
            };
            posts.push(post);
            displayPosts();
        };
        if (imageUpload) reader.readAsDataURL(imageUpload);
        else displayPosts();
    } else {
        alert("Please fill all the fields");
    }
});

// Function to display posts randomly
function displayPosts() {
    const postSection = document.getElementById('postSection');
    postSection.innerHTML = '';

    // Shuffle posts
    const shuffledPosts = posts.sort(() => 0.5 - Math.random());

    shuffledPosts.forEach((post, index) => {
        const postDiv = document.createElement('div');
        postDiv.className = 'post';
        postDiv.innerHTML = `
            <p><strong>${post.username}:</strong> ${post.postText}</p>
            ${post.image ? `<img src="${post.image}" alt="Post Image">` : ''}
            <div class="comment-section" id="comment-section-${index}">
                <input type="text" placeholder="Add a comment" id="commentInput-${index}">
                <button onclick="addComment(${index})">Comment</button>
            </div>
            <div class="comments" id="comments-${index}">
                ${post.comments.map(comment => `<p><strong>${comment.username}:</strong> ${comment.text}</p>`).join('')}
            </div>
        `;
        postSection.appendChild(postDiv);
    });
}

// Function to add comment to a post
function addComment(postIndex) {
    const commentInput = document.getElementById(`commentInput-${postIndex}`);
    const commentText = commentInput.value;
    const username = prompt("Enter your username to comment:");

    if (username && commentText) {
        posts[postIndex].comments.push({ username, text: commentText });
        displayPosts();
    }
}

// Search posts by username
document.getElementById('searchInput').addEventListener('input', (e) => {
    const searchQuery = e.target.value.toLowerCase();
    const filteredPosts = posts.filter(post => post.username.toLowerCase().includes(searchQuery));
    displayFilteredPosts(filteredPosts);
});

// Display filtered posts
function displayFilteredPosts(filteredPosts) {
    const postSection = document.getElementById('postSection');
    postSection.innerHTML = '';

    filteredPosts.forEach((post, index) => {
        const postDiv = document.createElement('div');
        postDiv.className = 'post';
        postDiv.innerHTML = `
            <p><strong>${post.username}:</strong> ${post.postText}</p>
            ${post.image ? `<img src="${post.image}" alt="Post Image">` : ''}
            <div class="comment-section" id="comment-section-${index}">
                <input type="text" placeholder="Add a comment" id="commentInput-${index}">
                <button onclick="addComment(${index})">Comment</button>
            </div>
            <div class="comments" id="comments-${index}">
                ${post.comments.map(comment => `<p><strong>${comment.username}:</strong> ${comment.text}</p>`).join('')}
            </div>
        `;
        postSection.appendChild(postDiv);
    });
}
