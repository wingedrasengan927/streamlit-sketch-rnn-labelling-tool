<template>
    <div>

        <canvas 
        id="canvas" 
        :width="args.width" 
        :height="args.height"
        @mouseleave="isDrawing=false"
        @mousedown="startDrawing"
        @mousemove="continueDrawing"
        @mouseup="stopDrawing"
        ref="canvas"></canvas>

        <div 
        class="btns"
        :style="{'max-width': args.width + 'px'}">
        <VueButton @click="clearCanvas" :isDisabled="isBtnDisabled">Clear Canvas</VueButton>
        <VueButton @click="finishDrawing" :isDisabled="isBtnDisabled">Finish Drawing</VueButton>
        </div>

    </div>    

</template>

<script>
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "../streamlit"

import VueButton from './VueButton.vue'

export default {
    name: 'SketchCanvas',
    data: function () {
        return {
            ctx: undefined,
            canDraw: true,
            isDrawing: false,
            myCanvas: undefined,
            prevX: 0,
            prevY: 0,
            data: [],
            isBtnDisabled: false,
        }
        
    },
    components: {
        VueButton
    },
    props: ["args"],
    mounted() {
        this.$nextTick(() => {
            this.myCanvas = this.$refs.canvas
            this.ctx = this.myCanvas.getContext('2d');
            this.ctx.lineWidth = 2;
            this.ctx.lineCap = "round";
        });
        console.log(this.args);
    },
    setup() {
        useStreamlit();
    },
    methods: {

        startDrawing(e) {
            if (this.canDraw) {

                this.isDrawing = true;

                const x = e.pageX - this.myCanvas.offsetLeft;
                const y = e.pageY - this.myCanvas.offsetTop;

                this.ctx.beginPath();
                this.ctx.moveTo(e.pageX - this.myCanvas.offsetLeft, e.pageY - this.myCanvas.offsetTop);

                this.data.push([x - this.prevX, y - this.prevY, 1, 0, 0]);
                this.prevX = x;
                this.prevY = y;
            }
        },
        continueDrawing(e) {
            if (this.isDrawing) {
                const x = e.pageX - this.myCanvas.offsetLeft;
                const y = e.pageY - this.myCanvas.offsetTop;

                this.ctx.lineTo(x, y);
                this.ctx.stroke();

                this.data.push([x - this.prevX, y - this.prevY, 1, 0, 0]);
                this.prevX = x;
                this.prevY = y;
            }
        },
        stopDrawing(e) {

            if (this.canDraw) {
                this.isDrawing = false;
                this.ctx.closePath();

                const x = e.pageX - this.myCanvas.offsetLeft;
                const y = e.pageY - this.myCanvas.offsetTop;

                this.data.push([x - this.prevX, y - this.prevY, 0, 1, 0]);
                this.prevX = x;
                this.prevY = y;
            }
        },
        clearCanvas() {
            this.ctx.clearRect(0, 0, this.myCanvas.width, this.myCanvas.height);
            this.data.length = 0;
        },
        finishDrawing() {
            this.isBtnDisabled = true;
            this.canDraw = false;

            this.data.push([0, 0, 0, 0, 1]);
            
            Streamlit.setComponentValue(JSON.parse(JSON.stringify(this.data)));
        }
    },
};
</script>

<style scoped>
    #canvas {
        border-style: dashed;
        border-color: rgb(200, 200, 200);
    }

  .btns {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }

</style>