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

        function clickButton(ev) {
            console.log('editor button click');
            // ev.preventDefault();
            const btn = ev.currentTarget;
            const dataset = btn.dataset;

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
            // const div = $(btnNode).siblings('div.status-selector');
            // const selector = div.children('select');
            // selector.toggle();
        }
        // <a class="btn btn-default" id='editor' href=""><span class="glyphicon glyphicon-pencil"></span></a> <
        // $('#editor').click(function(e) {
        //     e.preventDefault();
        //     $('#dropdown').toggle();
        // }); 
        // $('td[data-unitpk]').on("click", clickcell);
        let editorButtons = Array.from(document.querySelectorAll('.editor-button'));
        editorButtons.forEach(key => key.addEventListener('click', clickButton));
    });
})();
