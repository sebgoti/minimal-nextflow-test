params.input_image = "data/fixed.tiff"
params.sigma = "2.5,2.5"
params.outdir = "result"
params.dataset = ''

docker_img = "segonzal/minimal_skimage:0.22.0"

process BLUR {
    debug true

    container docker_img

    input:
    path(image_path)
    val(sigma)

    output:
    path('*.tiff')
    //path(outdir), emit: blurred
    // tuple val(meta), path(outdir), val(dataset), emit:

    script:
    def args = task.ext.args ?: ''
    """
    blur.py \
        -i $image_path \
        -s $sigma \
        -o $params.outdir \
        $args
    """
}

workflow {
    BLUR(
        channel.from(
        [
            [file(params.input_image, checkIfExists:true),],
        ]
        ),
        params.sigma
    )
}