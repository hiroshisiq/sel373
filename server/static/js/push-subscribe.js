const applicationServerPublicKey = 'BOJx5SrIq_6563OOrkaIVfsRpn-jtDnUwKEdMCJG23aKwCWFz-AL5qHEeotueAOHYxCFpg8xFrHiU9zxaPkdVRM';

let isSubscribed = false;
let swRegistration = null;

function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

if('PushManager' in window) {
  if ('serviceWorker' in navigator) {
    console.log('Service Worker and Push is supported');

    // Try to register service worker
    navigator.serviceWorker.register('/service-worker.js')
    .then(function(swReg) {
      // console.log('Service Worker is registered', swReg);
      swRegistration = swReg;
      initialiseUI();
    })
    .catch(function(error) {
      console.error('Service Worker Error', error);
    });
  // In case of Firefox
  } else {
    console.warn('serviceWorker is not supported');
  }
}

function initialiseUI() {
  if (isSubscribed) {
    // unsubscribeUser();
  } else {
    subscribeUser();
  }

  // Set the initial subscription value
  swRegistration.pushManager.getSubscription()
  .then(function(subscription) {
    isSubscribed = !(subscription === null);

    if (isSubscribed) {
      console.log('User is subscribed.');
    } else {
      console.log('User is NOT subscribed.');
    }

  });
}

function subscribeUser() {
  const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
  swRegistration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: applicationServerKey
  })
  .then(function(subscription) {
    // console.log('User is subscribed:', subscription);
    updateSubscriptionOnServer(subscription);
    isSubscribed = true;
  })
  .catch(function(err) {
    console.log('Failed to subscribe the user: ', err);
  });
}

function unsubscribeUser() {
  swRegistration.pushManager.getSubscription()
  .then(function(subscription) {
    if (subscription) {
      return subscription.unsubscribe();
    }
  })
  .catch(function(error) {
    console.log('Error unsubscribing', error);
  })
  .then(function() {
    updateSubscriptionOnServer(null);

    console.log('User is unsubscribed.');
    isSubscribed = false;
  });
}

function updateSubscriptionOnServer(subscription) {
  // TODO: Send subscription to application server
  // construct an HTTP request
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://143.107.235.44:8080/subscription', true);
  xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

  // send the collected data as JSON
  xhr.send(JSON.stringify(subscription));

  xhr.onloadend = function () {
    // done
  };

  console.log(JSON.stringify(subscription));
}
