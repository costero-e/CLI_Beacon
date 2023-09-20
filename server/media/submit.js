let secondInput = $('#id_mutated_allele'); // Cache the jQuery element
$("#id_region").on(
    "input propertychange",
    event => secondInput.prop(
        'disabled',
        event.currentTarget.value !== "")
);