document.addEventListener("DOMContentLoaded", function () {
  const copyButton = document.getElementById("copy-button");
  const resultList = document.getElementById("result-list");
  const clearResponse = document.getElementById("clear-response");
  const resultHeading = document.getElementById("result-heading");

  if (copyButton) {
    copyButton.addEventListener("click", function () {
      const textToCopy = Array.from(resultList.querySelectorAll("li"))
        .map((li) => li.textContent)
        .join("\n");

      const textarea = document.createElement("textarea");
      textarea.value = textToCopy;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);

      alert("Text copied to clipboard!");
    });
  }

  if (clearResponse) {
    clearResponse.addEventListener("click", function () {
      resultList.textContent = "";
      resultHeading.textContent = "";
      copyButton.style.visibility = "hidden";
      clearResponse.style.visibility = "hidden";
      window.location.href = "/";
    });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const resultList = document.getElementById("result-list");
  const clearResponseErr = document.getElementById("clear-response_err");
  const resultHeading = document.getElementById("result-heading");

  if (clearResponseErr) {
    clearResponseErr.addEventListener("click", function () {
      resultList.textContent = "";
      resultHeading.textContent = "";
      clearResponseErr.style.visibility = "hidden";
      window.location.href = "/";
    });
  }

  if (resultHeading) {
    let headingValue = resultHeading.innerHTML;
    if (headingValue === "WARNING!!!") {
      resultHeading.style.color = "red";
    }
  }
});
