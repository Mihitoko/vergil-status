chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'ANALYSE') {
    fetch(request.image)
      .then((res) => res.blob())
      .then((b) => {
        const formData = new FormData();
        formData.append('file', b, 'horny.png');
        fetch('http://localhost:3000', { method: 'POST', body: formData }).then(
          (r) => {
            r.json().then((result) => {
              sendResponse(result);
            });
          }
        );
      })
      .catch((r) => {
        console.log(r);
        sendResponse({});
      });
  }
  if (request.action === 'TRIGGER') {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      if (!tabs.length || !sender.tab || sender.tab.id !== tabs[0].id) {
        sendResponse(undefined);
        return;
      }
      chrome.tabs.sendMessage(
        tabs[0].id,
        { action: 'TRIGGER' },
        function (response) {}
      );
    });
    sendResponse(undefined);
  }
  return true;
});
