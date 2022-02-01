$.datetimepicker.setLocale('pl');
$('#date_start').datetimepicker({
    minDate: 0,
    format:'d-m-Y H:00',
    dayOfWeekStart: 1,
    theme:'dark',
});
$('#date_end').datetimepicker({
    minDate: 0,
    format:'d-m-Y H:00',
    dayOfWeekStart: 1,
    theme:'dark',
});

$(document).ready( function() {
    let ds = $('#date_start');
    let de = $('#date_end');
    if (ds.val() === "") {
        ds.datetimepicker({ value: new Date() });
    }
    if (de.val() === "") {
        de.datetimepicker({ value: '+1970/01/02' });
    }

    ds.change(function() {
        set_min_date();
    });

    function set_min_date() {
        let dateStart = ds.datetimepicker('getValue');
        let dateEnd = de.datetimepicker('getValue');
        let dateStartFormatted =  ds.val();
        if (dateEnd < dateStart ) {
            de.datetimepicker({ minDate: dateStart, value: dateStartFormatted, });
        } else {
            de.datetimepicker({ minDate: dateStart });
        }
    }
    $('.option_plus').click(function (e) {
        if (e.target === this) {
            $(this).find('.custom_checkbox').click();
        } else if ($(e.target).hasClass('item_options') || e.target.className === "option_label" || e.target.className === "option-description" || $(e.target).hasClass('option_payment') || $(e.target).is('p') || $(e.target).is('small') ) {
            $(this).find('.custom_checkbox').click();
        }
    })
});


// Calculations
$(function () {
    // Prices
    let extra_hours = 1/24;
    const rp_1_from = parseInt($("#period_from_1").val());
    const rp_1_to = parseInt($("#period_to_1").val()) + extra_hours;
    const rp_2_from = parseInt($("#period_from_2").val());
    const rp_2_to = parseInt($("#period_to_2").val()) + extra_hours;
    const rp_3_from = parseInt($("#period_from_3").val());
    const rp_3_to = parseInt($("#period_to_3").val()) + extra_hours;
    const rp_4_from = parseInt($("#period_from_4").val());
    const rp_4_to = parseInt($("#period_to_4").val()) + extra_hours;
    const price_1 = parseInt($("#rent_period_1").val());
    const price_2 = parseInt($("#rent_period_2").val());
    const price_3 = parseInt($("#rent_period_3").val());
    const price_4 = parseInt($("#rent_period_4").val());
    const limit_1 = parseInt($("#rent_period_limit_1").val());
    const limit_2 = parseInt($("#rent_period_limit_2").val());
    const limit_3 = parseInt($("#rent_period_limit_3").val());
    const limit_4 = parseInt($("#rent_period_limit_4").val());
    const price_month = parseInt($("#price_month").val());
    const deposit = parseInt($("#deposit").val());

    $( document ).ready(calculations());
    $("#date_start, #date_end, .change-price").change(calculations);

    function calculations() {
        // Default values
        let actual_deposit = 0;
        let extra_price_1 = 0;
        let extra_price_2 = 0;
        let extra_services = 0;
        let rent_price = 0;
        let promotion = 0;
        let final_price = 0;

        // Rent days
        let date1 = new Date($('#date_start').datetimepicker('getValue'));
        let date2 = new Date($('#date_end').datetimepicker('getValue'));
        date1.setMinutes(date1.getMinutes() - date1.getTimezoneOffset());
        date2.setMinutes(date2.getMinutes() - date2.getTimezoneOffset());
        let time1 = new Date($('#date_start').datetimepicker('getValue')).getHours();
        let time2 = new Date($('#date_end').datetimepicker('getValue')).getHours();

        let rent = Math.floor((date2.getTime() - date1.getTime()) / (1000 * 3600 * 24));
        let rent_not_round = (date2.getTime() - date1.getTime()) / (1000 * 3600 * 24);

        // non-working hours
        let dayOfWeek_1 = date1.getDay();
        let dayOfWeek_2 = date2.getDay()
        let dayOfWeek_field_1 = $('.non-working-hours-1');
        let dayOfWeek_field_2 = $('.non-working-hours-2');
        let workingHours_1 = dayOfWeek_1 !== 0 && dayOfWeek_1 !== 6 && (time1 >= 9 && time1 <= 19) || (dayOfWeek_1 === 6 && time1 >= 10 && time1 <= 15);
        let workingHours_2 = dayOfWeek_2 !== 0 && dayOfWeek_2 !== 6 && (time2 >= 9 && time2 <= 19) || (dayOfWeek_2 === 6 && time2 >= 10 && time2 <= 15);

        if ((!workingHours_1) && (!workingHours_2) ) {
            let non_working_hours_price = parseInt($('#before_non_working_hours').val()) + parseInt($('#after_non_working_hours').val());
            $('.non-working-hours').addClass('active');
            $('.non-working-hours.active').addClass('selected-option')
                .find('.op_item input')
                .attr('name', 'selected')
                .prop("checked", true)
                .val(non_working_hours_price + 'zł - Wynajem / zwrot auta poza godzinami pracy biura');
        } else if (!workingHours_1 || !workingHours_2) {
            let non_working_hours_price = parseInt($('#before_non_working_hours').val());
            $('.non-working-hours').addClass('active');
            $('.non-working-hours.active').addClass('selected-option')
                .find('.op_item input')
                .attr('name', 'selected')
                .prop("checked", true)
                .val(non_working_hours_price + 'zł - Wynajem / zwrot auta poza godzinami pracy biura');
        } else {
            $('.non-working-hours.active').removeClass('selected-option').find('.op_item input').attr('name', 'check').prop( "checked", false ).val(parseInt($('#before_non_working_hours').val()));
            $('.non-working-hours').removeClass('active');
        }

        // If weekend or non working hours, don't calculate extra day
        // if (!workingHours_1 || !workingHours_2 || $('.non-working-hours .custom_checkbox').is(':checked')) {
        //     $('.alert-extra-day').hide();
        //     if (rent <= 0 || isNaN(rent)) {
        //         rent = 1;
        //         $('#rent_days').val(1);
        //     } else {
        //         $('#rent_days').val(rent);
        //     }
        // // Else calculate extra day
        // } else {

            let extra_hours = Math.round((rent_not_round - rent) * 24)

            if (rent <= 0 || isNaN(rent)) {
                rent = 1;
                $('#rent_days').val(1);
                $('.alert-extra-day').hide();
            } else if (extra_hours <= 1) {
                $('#rent_days').val(rent);
                $('.alert-extra-day').hide();
            } else {
                rent += 1;
                $('#rent_days').val(rent);
                $('.alert-extra-day').show();
            }
            $('.alert-extra-day .close').click(function () {
                $('.alert-extra-day').hide();
            })
        // }

        // Extra services
        $('.option_plus input:checkbox, .option_plus input:radio').each(function () {
            if ($(this).is(':checked')) {
                $(this).closest( ".option_plus" ).addClass( "selected-option" );
            } else {
                $(this).closest( ".option_plus" ).removeClass( "selected-option" );
            }
        });
        $('.input_group input.per-day:checkbox:checked').each(function () {
            extra_price_1 += parseInt($(this).val());
        });
        $('.input_group input.per-rent:checkbox:checked').each(function () {
            extra_price_2 += parseInt($(this).val());
        });
        extra_services = extra_price_1 * rent + extra_price_2;
        $('#extra_services').val(extra_services);

        // Deposit
        if ($('#card').is(':checked')) {
            actual_deposit = 0;
            if ($('#rent_deposit').val()) {
                actual_deposit = $('#rent_deposit').val();
            }
            $('#actual_deposit').val(actual_deposit);
        } else{
            actual_deposit = deposit;
            $('#actual_deposit').val(actual_deposit);
        }

        // Final price calculation
        if (!workingHours_1 || !workingHours_2 || $('.non-working-hours .custom_checkbox').is(':checked')) {
            if (rent  < rp_2_from) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_1').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_1);
                $('#rent_period_2').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#rent_period_4').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_1;
                final_price = rent * price_1 + extra_services;
            } else if (rent >= rp_2_from && rent <= rp_2_to) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_2').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_2);
                $('#rent_period_1').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#rent_period_4').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_2;
                final_price = rent * price_2 + extra_services;
            } else if (rent >= rp_3_from && rent <= rp_3_to) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_3').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_3);
                $('#rent_period_1').attr('name','');
                $('#rent_period_2').attr('name','');
                $('#rent_period_4').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_3;
                final_price = rent * price_3 + extra_services;
            } else if (rent >= rp_4_from && rent <= rp_4_to) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_4').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_4);
                $('#rent_period_1').attr('name','');
                $('#rent_period_2').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_4;
                final_price = rent * price_4 + extra_services;
            } else if (rent >= 30) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#price_per_day_month').attr('name','price_day').show().val(Math.round(price_month / 30));
                $('#rent_period_limit').show().val(rent * limit_4);
                $('#rent_period_1').attr('name','');
                $('#rent_period_2').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#rent_period_4').attr('name','');
                rent_price =  rent * Math.round(price_month / 30);
                final_price = rent * Math.round(price_month / 30) + extra_services;
            }
        } else {
            if (rent_not_round  <= rp_1_to) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_1').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_1);
                $('#rent_period_2').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#rent_period_4').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_1;
                final_price = rent * price_1 + extra_services;
            } else if (rent_not_round > rp_1_to && rent_not_round <= rp_2_to) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_2').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_2);
                $('#rent_period_1').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#rent_period_4').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_2;
                final_price = rent * price_2 + extra_services;
            } else if (rent_not_round > rp_2_to && rent_not_round <= rp_3_to) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_3').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_3);
                $('#rent_period_1').attr('name','');
                $('#rent_period_2').attr('name','');
                $('#rent_period_4').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_3;
                final_price = rent * price_3 + extra_services;
            } else if (rent_not_round >= rp_3_to && rent_not_round <= rp_4_to) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#rent_period_4').attr('name','price_day').show();
                $('#rent_period_limit').show().val(rent * limit_4);
                $('#rent_period_1').attr('name','');
                $('#rent_period_2').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#price_per_day_month').attr('name','');
                rent_price = rent * price_4;
                final_price = rent * price_4 + extra_services;
            } else if (rent_not_round >= 30) {
                $('#price_intervals input, #limit_intervals input').each(function () {
                    $(this).hide();
                })
                $('#price_per_day_month').attr('name','price_day').show().val(Math.round(price_month / 30));
                $('#rent_period_limit').show().val(rent * limit_4);
                $('#rent_period_1').attr('name','');
                $('#rent_period_2').attr('name','');
                $('#rent_period_3').attr('name','');
                $('#rent_period_4').attr('name','');
                rent_price =  rent * Math.round(price_month / 30);
                final_price = rent * Math.round(price_month / 30) + extra_services;
            }
        }

        let regular_price = $("input[name=price_day]");
        promotion = (regular_price.next().val() - regular_price.val()) * rent;

        if (!workingHours_1) {
            dayOfWeek_field_1.removeClass('hide');
            if ($('#extra_services').length === 0) {
                final_price += parseInt($('#before_non_working_hours').val());
            }
        } else {
            if (!dayOfWeek_field_1.hasClass('hide')) {
                dayOfWeek_field_1.addClass('hide');
            }
        }
        if (!workingHours_2) {
            dayOfWeek_field_2.removeClass('hide');
            if ($('#extra_services').length === 0) {
                final_price += parseInt($('#after_non_working_hours').val());
            }
        } else {
            if (!dayOfWeek_field_2.hasClass('hide')) {
                dayOfWeek_field_2.addClass('hide');
            }
        }

        $('#rent_price').val(rent_price);
        $('#promotion').val('-'+promotion);
        $('#final_price').val(final_price);
    }
});

$(function () {
    $("#card, #cash").change(function () {
        var v = ($(this).val());
        if(v === 'card_payment'){
            $('.card_payment').show();
            document.getElementById('pay_cash').setAttribute('name','');
            document.getElementById('pay_card').setAttribute('name','pay');
            document.getElementById("card_number").required = true;
            document.getElementById("card_month").required = true;
            document.getElementById("card_year").required = true;
            document.getElementById("card_cvv").required = true;
            document.getElementById('card_pay_method').setAttribute('name', 'text_pay');
            document.getElementById('cash_pay_method').setAttribute('name', '');
            $('.cash_payment').hide();
        }
        else if (v === 'cash_payment'){
            $('.card_payment').hide();
            document.getElementById('pay_card').setAttribute('name','');
            document.getElementById('pay_cash').setAttribute('name','pay');
            document.getElementById("card_number").required = false;
            document.getElementById("card_month").required = false;
            document.getElementById("card_year").required = false;
            document.getElementById("card_cvv").required = false;
            document.getElementById('card_pay_method').setAttribute('name', '');
            document.getElementById('cash_pay_method').setAttribute('name', 'text_pay');
            $('.cash_payment').show();
        }
    })
});

$(".select").change(function() {
    var val = $(this).val();
    if( $(this).is(":checked") ) {
        this.setAttribute('name', 'selected');
    }
    else {
        this.setAttribute('name', '');
    }
});






