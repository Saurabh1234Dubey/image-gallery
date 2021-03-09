
	var validation = {
		validate_submit_action: function(b) {
			var submitAttemp = true;
			
			$(b).parents('form').find('.fvalidation').each((i, e) => {

                if( $(e).hasClass( "custom-validaion") ){

					if ($(e).val() == '') {
					  $(e).focus();
					  $(e).addClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('* This field cannot be blank.');
					  return submitAttemp = false;
					  event.preventDefault();
					} else {
					  $(e).removeClass('input-error').parent('div').css('position', 'relative').find('span.error-msg').html('');
					  submitAttemp = true;
					}
			
				  }

			});
			return submitAttemp;
		}
	}

	function submitFormValid(el){
		if (!validation.validate_submit_action(el)) {
				toastr.error('Please fill all the required information correctly.','Alert')
				return false
			} else {
				//showLoader();
				return true
			}
		}

	function submit_form(formId, submitId, msg){
		var valid = submitFormValid($("#"+submitId));
			if (valid){
				
				function show_popup(){
					$('#'+formId).submit()
			
					};
					setTimeout( show_popup, 1000 );
					toastr.success(msg,'Success')
				
			}
	}

