(function() {
    $(document).ready(function() {

        function clickcell(ev) {
            const dataset = ev.currentTarget.dataset;
            if (dataset) {
                let url = dataset.url;
                fetch(url, {
                        headers: {
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    })
                    .then(response => {
                        console.log(response);
                    })
                    .catch(function(reason) {
                        console.log(reason);
                    });
            }
        }

        $('td[data-unitpk]').on("click", clickcell);
    });
})();
