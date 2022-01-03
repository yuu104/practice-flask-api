{



  const btn = document.getElementById('btn');
  const uploading = () => {
    btn.disabled = true;
    btn.textContent = '作成中...';
  }

  const file = document.getElementById('file');
  const fileName = document.getElementById('file_name');
  const uploaded = () => {
    btn.disabled = false;
    btn.textContent = '作成';
    file.value = '';
    fileName.value = '';
    alert('作成が完了しました。');
  }

  const form = document.getElementById('form');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    uploading();
    let fd = new FormData();
    fd.append('file', file.files[0]);
    fd.append('fileName', fileName.value);

    fetch('/upload', {
      method: 'POST',
      body: fd
    })
    .then(res => res.json())
    .then(data => {
      if (data.result) {
        uploaded();
      } else {
        alert(data.message);
        btn.disabled = false;
        btn.textContent = '作成';
      }
    });
  });



}



