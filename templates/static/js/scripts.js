const deleteProduct = (id) => {
    fetch('/delete/' + id, {
        method: 'GET',
    }).then(() => {
        window.location.reload();
    });
}

const deleteProductView = (id) => {
    fetch('/delete-view/' + id, {
        method: 'GET',
    }).then(() => {
        window.location.href = '';
    });
}
