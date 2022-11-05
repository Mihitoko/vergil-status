let animationDidRun = false;

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'TRIGGER') {
    if (animationDidRun) {
      sendResponse(undefined);
      return;
    }
    animationDidRun = true;
    const video = document.createElement('video');
    video.controls = false;
    video.volume = 0.7;
    const src = document.createElement('source');
    src.src = chrome.runtime.getURL('assets/no_horny.webm');
    video.appendChild(src);
    video.classList.add('no_horny_vid');
    video.oncanplay = () => {
      console.log('READY');
      video.play();
    };

    const body = document.getElementsByTagName('body')[0];
    window.scrollTo(0, 0);
    body.classList.add('modify_body');
    body.insertBefore(video, body.firstChild);
    sendResponse(undefined);
    console.log('FINISCHED');
  }
});
