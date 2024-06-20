const deleteProduct = (id) => {
    fetch('/delete/' + id, {
        method: 'GET',
    }).then(() => {
        window.location.reload();
    });
}
