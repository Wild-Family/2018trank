"use strict";

window.onload = function() {

};

function click_post_ajax() {
    ajax_call("http://localhost:8000/api/ajax/test_post", "TEST", "POST")
        .then(
            (val) => {
                console.log(val);
                var json_obj = JSON.parse(val);
                return ajax_call("http://localhost:8000/api/ajax/test_post", json_obj.data, "POST")
            }
        )
        .then(
            (val) => {
                console.log(JSON.parse(val));
            }
        );
}