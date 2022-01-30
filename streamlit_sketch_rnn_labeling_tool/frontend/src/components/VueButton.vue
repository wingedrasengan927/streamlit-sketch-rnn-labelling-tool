<template>
    <button 
    @click="buttonClicked" 
    type="button" 
    class="btn"
    :disabled="isDisabled">
        <span class="btn__text"><slot></slot></span>
    </button>
</template>

<script>
export default {
    name: 'VueButton',
    props: {
        text: String,
        isDisabled: Boolean
    },
    methods: {
        buttonClicked() {
            this.$emit("click");
        }
    }
};
</script>

<style scoped>

    .btn {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50px;
        padding: 0px;
        margin: 6px 0;
        background: rgb(255, 124, 48);
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        border-radius: 5px;
        font-size: 16px;
        overflow: hidden;
        outline: none;
        border: none;
        cursor: pointer;
    }

    .btn:hover {
        background: rgb(255, 109, 25);
    }

    .btn:active {
        background: rgb(255, 94, 0);
    }

    .btn__text {
        color: white;
        padding: 6px 18px;
    }

    .btn:disabled {
        opacity: 0.75;
        cursor: not-allowed;
    }
    


</style>