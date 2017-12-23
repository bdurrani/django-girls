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
            ev.preventDefault();
            const btn = ev.currentTarget;
            const dataset = btn.dataset;

            if (dataset) {
                let url = dataset.url;
                let unitid = dataset.unitpk;
                let userid = dataset.userid;
                $.get(url, {
                        unitid: unitid,
                        userid: userid
                    },
                    function(data) {
                        console.log(data);
                        const available = $('#availability_' + unitid);
                        const currentuser = $('#current_user_' + unitid);
                        available.html(data.availability);
                        currentuser.html(data.username)
                        if (data.operation === 'checkout') {}
                        else {}
                    });
                // .done(function() {
                //     alert("second success");
                // })
                // .fail(function() {
                //     alert("error");
                // })

            }
        }

        function encodeQueryData(data) {
            let ret = [];
            for (let d in data)
                ret.push(encodeURIComponent(d) + '=' + encodeURIComponent(data[d]));
            return ret.join('&');
        }

        // let editorButtons = Array.from(document.querySelectorAll('.editor-button'));
        // editorButtons.forEach(key => key.addEventListener('click', clickButton));
    });
})();
