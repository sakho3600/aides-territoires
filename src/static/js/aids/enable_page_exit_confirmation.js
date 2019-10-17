(function (exports) {

    // Only requires exit confirmation if something was changed.
    exports.enableExitConfirmation = function(aidEditForm) {

        var initialData = aidEditForm.serialize();
        var eventAttached = false;

        aidEditForm.on('change', function() {

            // Don't bother if the event was already bound
            if (eventAttached) return;


            // Was some form data actually changed?
            var newData = aidEditForm.serialize();
            var changed = initialData != newData;
            if (changed) {

                // If so, bind the "onbeforeunload" event
                $(window).bind('beforeunload', function(){
                    return catalog.exit_confirmation;
                });
            }
        });
    };

})(this);

$(document).ready(function () {
    // Prevent status update when edit form was modified
    // to prevent data loss.
    var aidEditForm = $('form.main-form');

    enableExitConfirmation(aidEditForm);
});