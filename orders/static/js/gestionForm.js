(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Desea eliminar el elemento seleccionado?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

    document.getElementsByClassName("close")[0].onclick = function(event) {
       event.preventDefault();
       var alert = document.getElementsByClassName("close")[0].offsetParent.className.split(' ')[0];
       document.querySelector('.' + alert).classList.add('d-none')
    }
    
})();