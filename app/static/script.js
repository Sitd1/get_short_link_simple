async function shortenUrl() {
  const originalUrl = document.getElementById("originalUrl").value;
  if (!originalUrl) {
    alert("Please enter the original URL");
    return;
  }

  const response = await fetch("/shorten", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ original_url: originalUrl }),
  });

  const data = await response.json();
  if (data.short_url) {
    document.getElementById("shortUrl").innerText = data.short_url;
    document.getElementById("requestCount").innerText =
      "Request Count: " + data.request_count;
  }
}

document.getElementById("shortenButton").addEventListener("click", shortenUrl);
