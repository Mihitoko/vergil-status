'use strict';

const threshold = 0.5;
const interval = 2000;

const triggerVergil = () => {
  chrome.runtime.sendMessage(
    {
      action: 'TRIGGER',
    },
    (_) => {}
  );
};

const sleep = (duration) => {
  return new Promise((resolve) => {
    setTimeout(resolve, duration);
  });
};

const analyseImage = (image) => {
  return new Promise((resolve) => {
    chrome.runtime.sendMessage(
      { action: 'ANALYSE', image: image },
      (response) => {
        return resolve(response);
      }
    );
  });
};

const getVideoTags = () => {
  return document.getElementsByTagName('video');
};

const extractPicture = (video) => {
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  const canvasContext = canvas.getContext('2d');
  canvasContext.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
  return canvas.toDataURL();
};

const mainLoop = async () => {
  while (true) {
    await sleep(interval);
    const videos = getVideoTags();
    for (let i = 0; i < videos.length; i++) {
      const video = videos[i];
      if (video.classList.contains('no_horny_vid')) {
        continue;
      }
      const image = extractPicture(video);
      const result = await analyseImage(image);
      const res = result[0];
      console.log(res);
      if (res && (res.hentai > threshold || res.porn > threshold)) {
        console.log('TRIGGERED');
        video.pause();
        triggerVergil();
        // Exit the main loop, we don't want to analyse page further once
        // the video is triggered
        return;
      }
    }
  }
};

mainLoop().catch((e) => console.log(e));
