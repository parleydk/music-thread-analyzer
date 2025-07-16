// app.js
document.getElementById('threadForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const url = document.getElementById('redditURL').value;

  // TODO: Send URL to backend and get results
  console.log(`Analyzing: ${url}`);
});

