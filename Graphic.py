from matplotlib import pyplot as plt
import numpy as np
from matplotlib import colors


class Graphic:

    def graphic(self, segments, sizes, segment_classifier_size):
        fig, axes = plt.subplots(2, 2, figsize=(10, 6))

        """Draw segments"""
        for segment in segments:
            x = [segment.start.x, segment.end.x]
            y = [segment.start.y, segment.end.y]
            axes[0][0].plot(x, y, marker='o')
            axes[0][0].text(
                (segment.start.x+segment.end.x)/2,
                (segment.start.y + segment.end.y)/2,
                segment.name, fontsize=12
            )
        axes[0][0].set_title('Segments in the plane')
        axes[0][0].set_xlabel('X')
        axes[0][0].set_ylabel('Y')

        """Draw Total n. of permutations vs Size"""
        arr = np.array(sizes)
        labels, counts = np.unique(arr, return_counts=True)
        axes[0][1].bar(labels, counts, color='lightseagreen', lw=1, ec="black", align='center')
        axes[0][1].grid(True)
        axes[0][1].set_title('Total n. of permutations vs Size')
        axes[0][1].set_xlabel('Size BSP')
        axes[0][1].set_ylabel('Number of Permutations')

        """Draw Started minimum"""
        classified_sizes = list(segment_classifier_size.keys())
        max_size = np.max(classified_sizes)
        min_size = np.min(classified_sizes)

        max_size_occurences = segment_classifier_size[max_size]
        min_size_occurrences = segment_classifier_size[min_size]

        max_arr = np.array(max_size_occurences)
        labels_max, counts_max = np.unique(max_arr, return_counts=True)
        axes[1][1].bar(labels_max, counts_max, color='lightseagreen', lw=1, ec='black', align='center')
        axes[1][1].grid(True)
        axes[1][1].set_title('Maximal occurrence')
        axes[1][1].set_xlabel('Segment Name')
        axes[1][1].set_ylabel('Amount of permutations')

        min_arr = np.array(min_size_occurrences)
        labels_min, counts_min = np.unique(min_arr, return_counts=True)
        axes[1][0].bar(labels_min, counts_min, color='lightseagreen', lw=1, ec='black', align='center')
        axes[1][0].grid(True)
        axes[1][0].set_title('Minimal occurrence')
        axes[1][0].set_xlabel('Segment Name')
        axes[1][0].set_ylabel('Amount of permutations')

        plt.show()
